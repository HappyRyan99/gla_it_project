from django.urls import path
from rango import rangopages
import rango.rangopages.about
from rango import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', rangopages.about.index, name='about'),
    path('index', views.index, name='index'),
    path('images', rangopages.about.images, name='images'),
    path('about/', rangopages.about.about_path, name='about'),
    path('category/<slug:category_name_slug>/',
         views.show_category, name='show_category'),
    path('category/<slug:category_name_slug>/<int:page_num>',
         views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
]
