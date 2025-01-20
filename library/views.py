from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models
from django.views.generic import ListView
from django.views import generic

# Search
class SearchView(ListView):
    template_name = 'show.html'
    context_object_name = 'movie_list'
    
    def get_queryset(self):
        return models.Books.objects.filter(title__icontains=self.request.GET.get('q'))
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

#Список фильмов

class BooksListView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book_list'
    model = models.Books
    
    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

# def book_list(request):
#     if request.method == 'GET':
#         book_list = models.Books.objects.all().order_by('-id')
#         context = {'book_list': book_list}
#         return render(request, template_name='book.html', context=context)



class BooksDetailView(generic.DeleteView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'
    
    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(models.Books, id=todo_id)

# def book_detail(request, id):
#     if request.method == 'GET':
#         book_id = get_object_or_404(models.Books, id=id)
#         context = {'book_id': book_id}
#         return render(request, template_name='book_detail.html', context=context)







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