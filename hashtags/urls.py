from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.all_products, name='all_products'),
    path('fairy_tail_books/', views.fairy_tail_books, name='fairy_tail_books'),
    path('fantasy_books/', views.fantasy_books, name='fantasy_books'),
    path('dramma_books/', views.dramma_books, name='dramma_books'),
]
