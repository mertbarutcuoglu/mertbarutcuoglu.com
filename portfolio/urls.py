from . import views
from django.urls import path

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
]
