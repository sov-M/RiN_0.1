from django.shortcuts import render, redirect
from .models import Articles, ArticleImage  # Не забудьте импортировать ArticleImage
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy


def news_home(request):
    news = Articles.objects.order_by("price")
    return render(request, "news/news_home.html", {"news": news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = "news/details_view.html"
    context_object_name = "article"


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = "news/create.html"
    form_class = ArticlesForm

    def get_success_url(self):
        return reverse_lazy("news_home")


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = "/news"
    template_name = "news/news_delete.html"


def create(request):
    error = ""
    if request.method == "POST":
        form = ArticlesForm(request.POST, request.FILES)  # Добавлено request.FILES
        if form.is_valid():
            article = form.save()  # Сохраняем статью
            # Обрабатываем загрузку изображений
            images = request.FILES.getlist(
                "images"
            )  # Получаем все загруженные изображения
            for image in images:
                ArticleImage.objects.create(
                    article=article, image=image
                )  # Создаем записи для каждого изображения
            return redirect("news_home")
        else:
            error = "Ошибка"

    form = ArticlesForm()
    data = {"form": form, "error": error}
    return render(request, "news/create.html", data)
