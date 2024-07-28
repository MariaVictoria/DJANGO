from django.http import HttpResponse
from django.shortcuts import render
from .forms import CommentForm, ContactForm

def form(request):
    comment_form = CommentForm({'comment': 'Comentario', 'name': 'Vicky', 'url': 'https://www.instagram.com/vicky_gurumis/?hl=es'})
    return render(request, 'form.html', {'comment_form': comment_form})

def goal(request):
    if request.method != 'POST':
        return HttpResponse('El método POST no es soportado por esta ruta')
    return HttpResponse(request.POST['name'])

