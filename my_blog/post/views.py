from django.shortcuts import render

from .models import Author, Entry

# Create your views here.

def queries(request):

    #obtener todos los elementos 
    authors = Author.objects.all()
   
    #filtrado
    filtered = Author.objects.filter(name__icontains='food')
    
    #seleccionar un unico elemento
    author = Author.objects.get(id=1)

    #limitacion de los 10 primeros elementos
    limits = Author.objects.all()[:10]

    #obtener 5 entradas saltando los primeros 5 offset

    skiping = Author.objects.all()[5:10]

    #obtener todos los elementos cuyo id sea menor o igual a 15

    filtered2 = Author.objects.filter(id__lte=15)

#----------- ORDER BY -----------------

    #ordenamiento ascendente
    asc = Author.objects.order_by('email')

    #ordenamiento descendente
    desc = Author.objects.order_by('email')


    return render(request, 'post/queries.html', {'authors': authors, 'filtered': filtered,'author': author, 'limits': limits, 'skiping': skiping, 'asc': asc, 'desc': desc, 'filtered2': filtered2})
