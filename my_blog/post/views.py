from django.shortcuts import render
from .models import Author, Entry
from django.http import HttpResponse

# Create your views here.

def update (request):   
    author = Author.objects.get(id=1)

    author.name = 'Arturo'
    author.email = 'arturo@demo.com'
    author.save()
    return HttpResponse('Se actualizo el autor')


def queries(request):

    #obtener todos los elementos 
    authors = Author.objects.all()
   
    #filtrado
    filtered = Author.objects.filter(name__icontains='food')

    #obtener todos los elementos cuyo id sea menor o igual a 15

    filtered2 = Author.objects.filter(id__lte=15)
    
    #seleccionar un unico elemento
    author = Author.objects.get(id=1)

    #limitacion de los 10 primeros elementos
    limits = Author.objects.all()[:10]

    #obtener 5 entradas saltando los primeros 5 offset

    skiping = Author.objects.all()[5:10]

#----------- ORDER BY -----------------

    #ordenamiento ascendente
    asc = Author.objects.order_by('email')

    #ordenamiento descendente
    desc = Author.objects.order_by('email')


    return render(request, 'post/queries.html', {'authors': authors, 'filtered': filtered,'author': author, 'limits': limits, 'skiping': skiping, 'asc': asc, 'desc': desc, 'filtered2': filtered2})


