from django.shortcuts import render
from . import models

# Общий список продуктов
def all_products(request):
    if request.method ==  'GET':
        all_products = models.Product.objects.all()
        context = {'all_products': all_products}
        return render(request, template_name='hashtags/all_products.html', context=context)

# Список сказок
def fairy_tail_books(request):
    if request.method == 'GET':
        drink_products = models.Product.objects.filter(tags__name='Сказки')
        context = {'fairy_tail_books': fairy_tail_books}
        return render(request, template_name='hashtags/fairy_tail_books.html', context=context)
    
# Список фантастики
def fantasy_books(request):
    if request.method == 'GET':
        eat_products = models.Product.objects.filter(tags__name='Фатастика')
        context = {'fantasy_books': fantasy_books}
        return render(request, template_name='hashtags/fantasy_books.html', context=context)
    
# Список драмм
def dramma_books(request):
    if request.method == 'GET':
        eat_products = models.Product.objects.filter(tags__name='Драмма')
        context = {'dramma_books': dramma_books}
        return render(request, template_name='hashtags/dramma_books.html', context=context)
    