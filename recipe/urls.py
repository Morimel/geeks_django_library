from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.recipe_list, name='recipe_list'),
    path('recipe/new/', views.create_recipe, name='create_recipe'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:pk>/delete/', views.delete_recipe, name='delete_recipe'),
]
