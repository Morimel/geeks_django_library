from django.shortcuts import render
from . import models
from django.views import generic

# Общий список продуктов

class AllBooksView(generic.ListView):
    template_name = 'hashtags/all_products.html'
    context_object_name = 'all_products'
    model = models.Product
    
    def get_queryset(self):
        return self.model.objects.all()


# def all_products(request):
#     if request.method ==  'GET':
#         all_products = models.Product.objects.all()
#         context = {'all_products': all_products}
#         return render(request, template_name='hashtags/all_products.html', context=context)

# Список сказок

class FairyTailBooksView(generic.ListView):
    template_name = 'hashtags/fairy_tail_books.html'
    context_object_name = 'fairy_tail_books'
    model = models.Product
    
    def get_queryset(self):
        return self.model.objects.filter(tags__name="Сказки")


# def fairy_tail_books(request):
#     if request.method == 'GET':
#         fairy_tail_books = models.Product.objects.filter(tags__name='Сказки')
#         context = {'fairy_tail_books': fairy_tail_books}
#         return render(request, template_name='hashtags/fairy_tail_books.html', context=context)
    
    
    
# Список фантастики
class FantasyBooksView(generic.ListView):
    template_name = 'hashtags/fantasy_books.html'
    context_object_name = 'fantasy_books'
    model = models.Product
    
    def get_queryset(self):
        return self.model.objects.filter(tags__name="Фатастика")

# def fantasy_books(request):
#     if request.method == 'GET':
#         fantasy_books = models.Product.objects.filter(tags__name='Фатастика')
#         context = {'fantasy_books': fantasy_books}
#         return render(request, template_name='hashtags/fantasy_books.html', context=context)
    
# Список драмм

class DrammaBooksView(generic.ListView):
    template_name = 'hashtags/dramma_books.html'
    context_object_name = 'dramma_books'
    model = models.Product
    
    def get_queryset(self):
        return self.model.objects.filter(tags__name="Драмма")


# def dramma_books(request):
#     if request.method == 'GET':
#         dramma_books = models.Product.objects.filter(tags__name='Драмма')
#         context = {'dramma_books': dramma_books}
#         return render(request, template_name='hashtags/dramma_books.html', context=context)
    