from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def oldpasswords(request):
    return render(request, 'generator/oldpasswords.html')


def password(request, oldlist=()):
    characters = list('abcdefghigklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIGKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    lenght = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(characters)
        newpassword.insert(0, thepassword)

    return render(request, 'generator/password.html', {'password': thepassword})
    return render(request, 'generator/oldpasswords.html', {'password': newpassword})
