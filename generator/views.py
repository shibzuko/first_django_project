from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    numbers = list('0123456789')
    stringUp = list('ASDFGHJKLZXCVBNMQWERTYUIOP')
    stringLu = list('asdfghjklzxcvbnmqwertyuiop')
    spec = list('!@#$%^&*?')
    lenght = int(request.GET.get('lenght'))
    new_password = ''

    if request.GET.get('uppercase'):
        stringLu.extend(stringUp)

    if request.GET.get('numbers'):
        stringLu.extend(numbers)

    if request.GET.get('special'):
        stringLu.extend(spec)

    for i in range(lenght):
        new_password += random.choice(stringLu)


    return render(request, 'generator/password.html', {'password': new_password})


def about(request):
    return render(request, 'generator/about.html')