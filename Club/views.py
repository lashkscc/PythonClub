from django.shortcuts import render
from .models import Resource

# Create your views here.
def index(request): 
    return render(request,  'Club/index.html')

def resources(request):
    resource_list=Resource.objects.all()#bad for big lists, use find instead
    return render(request, 'Club/resources.html', {'resource_list': resource_list})