from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('all_tours', views.all_tours, name="all_tours"),
    path('hot_tours', views.hot_tours, name="hot_tours"),
    path('blog', views.blog, name="blog"),
    path('search_tour', views.in_search, name="search_tour"),
]