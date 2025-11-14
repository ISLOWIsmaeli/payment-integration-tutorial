from django.shortcuts import render
from .models import Project
from django.shortcuts import get_object_or_404

# Create your views here.
def project_home(request):
    projects = Project.objects.all()
    return render(request, "projectsApp/projects.html", {"projects": projects})


def donation(request, pk):
    """Show project details and a link to the payment page for this project."""
    project = get_object_or_404(Project, pk=pk)
    return render(request, "projectsApp/donation_checkout.html", {"project": project})