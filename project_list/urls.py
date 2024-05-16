from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("html/", views.html, name="html"),
    path("css/", views.css, name="css"),
    path("js/", views.javascript, name="javascript"),
    path("python/", views.python, name="python"),
    path("pong/", views.pong, name="pong"),
]