from django.http import HttpResponse
from django.shortcuts import render
import countryinfo
from .models import *

def index(request):
    country = countryinfo.CountryInfo("Aruba")
    info = country.info()
    key_list = info.values()
    cont = Continents.objects.all()
    return render(request, 'country_info/index.html', context={'title': "Info about country", 'info': info, 'key_list': key_list, 'cont': cont})

def inform(request, name):
    info = Continents.objects.filter(continent=name)
    return render(request, 'country_info/more_info.html', context={'info': info, 'title': "Info about continent"})