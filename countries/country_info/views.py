from django.http import HttpResponse
from django.shortcuts import render
import countryinfo
from .models import *

def index(requests):
    country = countryinfo.CountryInfo("Aruba")
    info = country.info()
    key_list = info.values()
    cont = Continents.objects.all()
    return render(requests, 'country_info/index.html', context={'title': "Info about country", 'info': info, 'key_list': key_list, 'cont': cont})

def inform(request, name):
    print(request.GET)
    return HttpResponse(f'<p>{name}</p>')