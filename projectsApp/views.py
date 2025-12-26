from django.shortcuts import render
from .models import Project
from django.shortcuts import get_object_or_404

# Create your views here.
def project_home(request):
    projects = Project.objects.all()
    return render(request, "projectsApp/projects.html", {"projects": projects})

