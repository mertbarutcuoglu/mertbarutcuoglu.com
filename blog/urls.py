from . import views
from django.urls import path

urlpatterns = [
    path('blog/', views.PostList.as_view()),
    #path('blog/<slug:slug>/',)
]
