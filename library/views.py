from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

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