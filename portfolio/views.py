from django.views import generic
from .models import Project


class ProjectList(generic.ListView):
    queryset = Project.objects.order_by('id')
    template_name = 'projects.html'