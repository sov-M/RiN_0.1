from django.shortcuts import render, redirect
from .models import Articles, ArticleImage  # Не забудьте импортировать ArticleImage
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy


def products_home(request):
    products = Articles.objects.order_by("price")

    if request.method == "POST":
        action = request.POST.get("action")
        if action == "-price":
            products = Articles.objects.order_by("-price")
        elif action == "load_obuvnoy-rojok":
            products = Articles.objects.filter(category="obuvnoy-rojok")
        elif action == "load_obuvnoy-mech":
            products = Articles.objects.filter(category="obuvnoy-mech")
        elif action == "load_nabor":
            products = Articles.objects.filter(category="nabor")
        elif action == "load_podves":
            products = Articles.objects.filter(category="podves")
        elif action == "load_kobura":
            products = Articles.objects.filter(category="kobura")
        elif action == "load_nojny":
            products = Articles.objects.filter(category="nojny")
        elif action == "load_gardy":
            products = Articles.objects.filter(category="gardy")
        elif action == "load_upakovka":
            products = Articles.objects.filter(category="upakovka")
        elif action == "reset":
            products = Articles.objects.order_by("price")

    return render(request, "products/products_home.html", {"products": products})


class ProductsDetailView(DetailView):
    model = Articles
    template_name = "products/details_view.html"
    context_object_name = "article"


class ProductsUpdateView(UpdateView):
    model = Articles
    template_name = "products/create.html"
    form_class = ArticlesForm

    def get_success_url(self):
        return reverse_lazy("products_home")


class ProductsDeleteView(DeleteView):
    model = Articles
    success_url = "/products"
    template_name = "products/products_delete.html"


def create(request):
    error = ""
    if request.method == "POST":
        form = ArticlesForm(request.POST, request.FILES)  # Добавлено request.FILES
        if form.is_valid():
            article = form.save()  # Сохраняем статью
            images = request.FILES.getlist(
                "images"
            )  
            for image in images:
                ArticleImage.objects.create(
                    article=article, image=image
                ) 
            return redirect("create")
        else:
            error = "Ошибка"

    form = ArticlesForm()
    data = {"form": form, "error": error}
    return render(request, "products/create.html", data)
