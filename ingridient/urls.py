from django.urls import path
from . import views

urlpatterns = [
    path('ingredient/add/<int:recipe_id>/', views.add_ingredient, name='add_ingredient'),
]
