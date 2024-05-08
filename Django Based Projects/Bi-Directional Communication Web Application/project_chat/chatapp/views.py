from django.shortcuts import render, redirect, HttpResponse
from .models import *
# Create your views here.
def CreateRoom(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        room_name= request.POST.get('room')

        try:
            get_room = Room.objects.get(room_name = room_name)

            context = {
            'username':username,
            'room_name':get_room,
        }
            
            return render (request, 'message.html', {
                'context':context
                })
        
        except Room.DoesNotExist:
            
            Room.objects.create(
                room_name = room_name
            )

            context = {
                'username':username,
                'room_name':get_room,
            }

        return render(request, 'message.html', {
            'context':context
            }) 
    
    else:
        return render(request, 'message.html') 

# This view will allow users to share messages with eachother. 
def MessageView(request, room_name, username):
    get_room = Room.objects.get(room_name = room_name)
    get_message = Messages.objects.filter(room = get_room)

    context = {
        'messages' : get_message,
        'user' : username,
        'room_name' : room_name
    }
    return render(request, 'message.html', context)

    '''
    The room name and the username will both be passed from 
    the create room view. They will then be sent to this view and passed as agruments
    
    '''



