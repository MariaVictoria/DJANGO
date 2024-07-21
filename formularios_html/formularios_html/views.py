from django.shortcuts import render
from django.http import HttpResponse

# Create your views here: renderizamos la plantilla. primero pasamos la request, luego pasamos en la url el nombre de la vista (plantilla) y el contexto
def getform (request):
    return render (request, 'form.html',{})

def getgoal (request):
    '''
    if request.method == 'GET':
       return render (request, 'success.html',{})

    else:
        return HttpResponse (' El method POST no es soportado por esta ruta')
        
    '''
    if request.method != 'GET':
        return HttpResponse (' El method POST no es soportado por esta ruta')
    
    name=request.GET['name']

    return render (request, 'success.html',{'name':name})


def postform (request):
    return render(request, 'postform.html', {})
    

def postgoal (request):
    if request.method != 'POST':
        return HttpResponse (' El méthod GET no es soportado por esta ruta')

    info=request.POST['info']

    return render(request, 'postsuccess.html', {'info':info})

    
    