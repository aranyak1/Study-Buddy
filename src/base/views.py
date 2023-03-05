from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id':1,'name':'let''s learn python'},
    {'id': 2, 'name': 'let''s learn django'},
    {'id': 3, 'name': 'Frontend'},
         ]

def home(request):
    context = {'rooms': rooms}
    return render(request,'home.html',context)


def room(request,pk):
    room = None
    for el in rooms:
        if el['id'] == int(pk):
            room = el
    context = {'room':room}

    return render(request, 'room.html',context)
