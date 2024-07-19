from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

# Create your views here.
def test(request):
    return HttpResponse("Funciona correctamente")

def create(request):
    #comment= Comment(name='Juan',score= 5,comment='muy bueno',date='2022-10-10')
    #comment.save()
    #comment= Comment.objects.create(name='a')
    return HttpResponse("Ruta para comprobar la creación de modelos")

def delete(request):
    comment= Comment.objects.get(id=17)
    #comment.delete()
    #Comment.objects.all().delete()
    #Comment.objects.filter(name='a').delete()
      
    Comment.objects.filter(id__in=[5,6,7,8,9,14,15,16]).delete()
    return HttpResponse("Ruta para comprobar la eliminación de modelos")