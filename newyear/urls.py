from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.newyear),
    path("", views.index)
    ]