from django.shortcuts import render, redirect
from django.urls import reverse
from csv import DictReader
from django.conf import settings
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as file:
        reader = DictReader(file)
        data = [name for name in reader]
        current_page = request.GET.get('page', 1)
        paginator = Paginator(data, 10)
        page = paginator.get_page(current_page)
        context = {
            'bus_stations': page,
            'page': page,
        }
        return render(request, 'stations/index.html', context)
