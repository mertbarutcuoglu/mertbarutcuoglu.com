from django.contrib import admin
from django.urls import path, include

from portfolio.views import ProjectList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
]
