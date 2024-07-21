from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date

# Create your views here.
def create(request):
    # Create and save the Reporter instance
    rep = Reporter(first_name='Ale', last_name='Man', email='a@a.com')
    rep.save()
    
    # Create and save Article instances
    art1 = Article(headline='muy bueno ', pub_date=date(2022, 5, 5), reporter=rep)
    art1.save()
    art2 = Article(headline='so good ', pub_date=date(2019, 8, 7), reporter=rep)
    art2.save()
    art3 = Article(headline='nice ', pub_date=date(2000, 9, 5), reporter=rep) 
    art3.save()
    art4 = Article(headline='bad ', pub_date=date(2024, 10, 5), reporter=rep)
    art4.save()

    #query = art4.reporter.first_name
    #query= rep.article_set.all()
    #query =rep.article_set.filter(headline='nice '  ) 
    query = rep.article_set.count()
    

    return HttpResponse(query)
