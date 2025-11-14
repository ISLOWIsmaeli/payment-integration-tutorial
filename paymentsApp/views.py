from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


import uuid
from django.urls import reverse

from django.contrib import messages
from projectsApp.models import Project

# Create your views here.
def payments_home(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, "paymentsApp/payments.html", {"project": project})
