from django.http import HttpResponse
from django.shortcuts import render
import countryinfo


def index(requests):
    country = countryinfo.CountryInfo("Aruba")
    info = country.info()
    key_list = info.values()
    return render(requests, 'country_info/index.html', context={'title': "Info about country", 'info': info, 'key_list': key_list})
