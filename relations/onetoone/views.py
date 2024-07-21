from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant
# Create your views here.

def create(request):    
    #creacion de elementos
    place = Place(name='Casa sum', address='Ser 123') 
    place.save()

    restaurant = Restaurant(place=place, number_Employees=10)
    restaurant.save()


    return HttpResponse(restaurant.place.name)