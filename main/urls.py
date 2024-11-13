from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("admin", views.admin, name="admin"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]
