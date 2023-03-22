import random

from django.http import HttpResponse
from django.shortcuts import render
import countryinfo
from .models import *
from .static.country_info.others.list_of_country import list_of_countries
from random import choice

def index(request):
    #list_of_countries = ['Botswana', 'usa', 'canada']
    country = countryinfo.CountryInfo(random.choice(list_of_countries))
    info = country.info()
    key_list = info.values()
    cont = Continents.objects.all()
    return render(request, 'country_info/index.html', context={'title': "Info about country", 'info': info, 'key_list': key_list, 'cont': cont})

def inform(request, name):
    info = Continents.objects.filter(continent=name)
    cont = Continents.objects.all()
    return render(request, 'country_info/more_info.html', context={'info': info, 'title': "Info about continent", 'cont': cont})