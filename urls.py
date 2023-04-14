from django.urls import path,include
from . import views

app_name = "tasks"
urlpatterns = [
    path("tasks/", views.tasks, name="tasks"),
    path("add/", views.add, name="add")

]