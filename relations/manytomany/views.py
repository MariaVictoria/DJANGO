from django.shortcuts import render
from django.http import HttpResponse
from .models import Publication, Article

def create(request):
 # Create and save Articles
    art1 = Article(headline='articulo primero')
    art1.save()

    art2 = Article(headline='articulo segundo')
    art2.save()

    art3 = Article(headline='articulo tercero')
    art3.save()

    # Create and save Publications
    publi1 = Publication(title='publicacion primero')
    publi1.save()
    publi2 = Publication(title='publicacion segundo')
    publi2.save()
    publi3 = Publication(title='publicacion tercero')
    publi3.save()
    publi4 = Publication(title='publicacion cuarto')
    publi4.save()
    publi5 = Publication(title='publicacion quinto')
    publi5.save()
    publi6 = Publication(title='publicacion sexto')
    publi6.save()
    publi7 = Publication(title='publicacion septimo')
    publi7.save()

    # Associate Publications with Articles
    art1.publications.add(publi1, publi2, publi7)
    art2.publications.add(publi3, publi4)
    art3.publications.remove(publi5)

    query = art1.publications.all()

    #publi1=Publication.objects.get(id=1)
    #query = publi1.article_set.all()   
    

    return HttpResponse(query)
