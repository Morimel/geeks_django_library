from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models


#Список фильмов
def book_list(request):
    if request.method == 'GET':
        book_list = models.Books.objects.all().order_by('-id')
        context = {'book_list': book_list}
        return render(request, template_name='book.html', context=context)


def book_detail(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Books, id=id)
        context = {'book_id': book_id}
        return render(request, template_name='book_detail.html', context=context)







# Create your views here.

def about_me(request):
    if request.method == 'GET':
        return HttpResponse('Hello, my name is Isa')
    
def about_my_pets(request):
    if request.method == 'GET':
        return HttpResponse('Hello, my pets name is Bell')
    
def time(request):
    if request.method == 'GET':
        current_time = datetime.now().time()
        return HttpResponse(f'{current_time}')