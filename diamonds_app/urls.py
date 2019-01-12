from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index.html$', views.index, name='index'),
    url(r'^blog/', views.blog, name='blog'),
    url(r'^about', views.about, name='about'),
    url(r'^result/', views.result),
]
