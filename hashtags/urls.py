from django.urls import path
from . import views

urlpatterns = [
    path('all_products/', views.AllBooksView.as_view(), name='all_products'),
    path('fairy_tail_books/', views.FairyTailBooksView.as_view(), name='fairy_tail_books'),
    path('fantasy_books/', views.FantasyBooksView.as_view(), name='fantasy_books'),
    path('dramma_books/', views.DrammaBooksView.as_view(), name='dramma_books'),
]
