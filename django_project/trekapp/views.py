# from django import template
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Trek

# homepage.
def home(request):
    return render(request, 'trekapp/home.html')

# trek details
def trekDetail(request, trek_id):
    trek_list = Trek.objects.get(pk=trek_id)
    context = {
        'trek_list': trek_list,
    }
    return render(request, 'trekapp/index.html', context)

def profile(request, username):
    return HttpResponse("Profile page of User : {0}".format(username))

def login(request):
    return render(request, 'trekapp/login.html')

def dologin(request):
    return redirect('/')