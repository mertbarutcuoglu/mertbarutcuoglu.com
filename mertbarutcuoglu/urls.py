from django.contrib import admin
from django.urls import path

from portfolio.views import projects_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects', projects_view),
]
