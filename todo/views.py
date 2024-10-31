# todo/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'todo/home.html')  # Stelle sicher, dass die Vorlage existiert
