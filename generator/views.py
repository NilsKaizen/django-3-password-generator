from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password':'987w9de98h9he'})

def password(request):

    thepassword = ''

    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    special = list(string.punctuation)
    numbers = list(string.digits)

    character = [lower]

    length = int(request.GET.get('length', 12))
    u = request.GET.get('uppercase')
    s = request.GET.get('special')
    n = request.GET.get('numbers')

    if u == 'on':
        character.append(upper)
    if s == 'on':
        character.append(special)
    if n == 'on':
        character.append(numbers)

    for i in range(length):
        char = random.choice(character)
        thepassword += random.choice(char)


    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')