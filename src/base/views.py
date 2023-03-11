from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm
# Create your views here.

# rooms = [
#     {'id':1,'name':'let''s learn python'},
#     {'id': 2, 'name': 'let''s learn django'},
#     {'id': 3, 'name': 'Frontend'},
#          ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request,'home.html',context)


def room(request,pk):
    room = Room.objects.get(id=pk)
    # for el in rooms:
    #     if el['id'] == int(pk):
    #         room = el
    context = {'room':room}

    return render(request, 'room.html',context)

def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request,'room_form.html',context)