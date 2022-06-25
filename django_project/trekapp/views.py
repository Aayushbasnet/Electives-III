# from django import template
from django.http import HttpResponse
from django.shortcuts import render
from .models import Trek

# homepage.
def home(request):
    return HttpResponse("Hello World !")

# trek details
def trekDetail(request, trek_id):
    trek_list = Trek.objects.get(pk=trek_id)
    context = {
        'trek_list': trek_list,
    }
    return render(request, 'trekapp/index.html', context)

