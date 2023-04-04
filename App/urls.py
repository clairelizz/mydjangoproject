from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.eMobilis),
    path("home", views.home)
]