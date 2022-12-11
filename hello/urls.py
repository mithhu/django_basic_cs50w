from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("mithhu", views.mithhu, name="mithhu"),
    path("<str:name>", views.greet, name="greet")
]