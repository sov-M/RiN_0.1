from django import forms
from .models import Articles, ArticleImage


class ArticleImageForm(forms.ModelForm):
    class Meta:
        model = ArticleImage
        fields = ["image"]


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = [
            "category",
            "name",
            "remains",
            "thickness",
            "length",
            "weight",
            "description",
            "price",
            "set",
            "cover",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Название товара"}
            ),
            "remains": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Остаток на складе"}
            ),
            "thickness": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Толщина (0.0 мм)"}
            ),
            "length": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Длина (0.0 см)"}
            ),
            "weight": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Вес (0.0 гр)"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Описание"}
            ),
            "price": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Цена (0 руб.)"}
            ),
            "set": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Комплектация"}
            ),
            "cover": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }
