from django.shortcuts import render
from .models import Project

def projects_view(request, *args, **kwargs):
    projects = Project.objects.order_by('id')
    return render(request, "projects.html", {'projects': projects})

