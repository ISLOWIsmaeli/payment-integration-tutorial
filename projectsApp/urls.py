from django.urls import path, re_path
from . import views
urlpatterns = [
    path("projects/", views.project_home, name="project-home"),
]