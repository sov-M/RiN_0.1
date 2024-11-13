from django.db import models

CATEGORY_CHOICES_category = [
    ("obuvnoy-rojok", "Обувной рожок"),
    ("obuvnoy-mech", "Обувной меч"),
    ("nabor", "Наборы"),
    ("podves", "Подвес"),
    ("kobura", "Кобура"),
    ("nojny", "Ножны"),
    ("gardy", "Гарды"),
    ("upakovka", "Упаковка"),
    ("other", "Другое"),
]

class ArticleImage(models.Model):
    article = models.ForeignKey(
        "Articles", related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="images/articles/")


class Articles(models.Model):
    category = models.CharField(
        "Категория товара", max_length=70, choices=CATEGORY_CHOICES_category, blank=True
    )
    name = models.CharField("Название товара", max_length=270, blank=True)
    remains = models.CharField("Остаток на складе", max_length=270, blank=True)
    thickness = models.CharField("Толщина товара", max_length=270, blank=True)
    length = models.CharField("Длина товара", max_length=270, blank=True)
    weight = models.CharField("Вес товара", max_length=270, blank=True)
    description = models.TextField("Описание товара", blank=True)
    set = models.CharField("Комплект товара", max_length=270, blank=True)
    price = models.CharField("Цена товара", max_length=270, blank=True)
    cover = models.ImageField(upload_to='images/post', blank=True)
    date = models.DateTimeField("Дата добавления", auto_now_add=True)  

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/news/{self.id}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
