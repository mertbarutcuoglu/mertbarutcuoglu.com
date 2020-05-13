from django.contrib import admin
from django.urls import path, include
from homepage.views import homepage_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_view),
    path('', include('portfolio.urls')),
    path('', include('blog.urls')),
]
