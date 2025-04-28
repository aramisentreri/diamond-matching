from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('about', views.about, name='about'),
    path('result/', views.result),
]
