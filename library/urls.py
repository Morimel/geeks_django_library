from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book_detail/<int:id>/', views.book_detail, name='book_detail'),
    path('about-me/', views.about_me, name='about-me'),
    path('about-pet/', views.about_my_pets, name='about-pet'),
    path('time/', views.time, name='time')
]
