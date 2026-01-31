from django.urls import path
from rango import rangopages
import rango.rangopages.about
from rango import views

urlpatterns = [
    path('', views.page_not_found, name='page_not_found'),
    path('about', rangopages.about.index, name='about'),
    path('index', views.index, name='index'),
    path('images', rangopages.about.images, name='images'),
    path('about/', rangopages.about.about_path, name='about'),
    path('category/<slug:category_name_slug>/',
         views.show_category, name='show_category'),
]
