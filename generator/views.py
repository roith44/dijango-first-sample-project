from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
   return render(request, 'generator/home.html')
def about(request):
    return render(request, 'generator/about.html')
   
def newpass(request):
   char = list('abcdefghijklmnopqrstuvwxyz')
   length = int(request.GET.get('length', 8))
   if request.GET.get('uppercase'):
      char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
   if request.GET.get('number'):
      char.extend(list('1234567890'))
   if request.GET.get('special'):
      char.extend(list('!@#$%^&*()'))
   test = ''
   for x in range(length):
      test += random.choice(char)
   return render(request, 'generator/password.html' , {'password': test})