from django.http import Http404, HttpResponse
from django.shortcuts import render
import datetime

def index(request):
	return render(request, "comingsoon.html")
	
def hello(request):
	return render(request, "hello.html")

def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'hours_ahead.html', {'hour_offset': offset, 'next_time': dt})

def display_meta(request):
    meta_values = request.META.items()
    meta_values.sort()
    return render(request, 'display_meta.html', {'meta_information': meta_values})