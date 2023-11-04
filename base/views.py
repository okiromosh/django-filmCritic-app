from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db.models import Count

# Create your views here.


# User Views

def loginPage(request):
    page = 'login'
    # stops an already logged in user from login in again
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'Username OR Password is not correct!')
    context = {
        'page': page,
    }
    return render(request, 'base/login-register.html', context)


def registerPage(request):
    page = 'register'

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Save the user object
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            # You can also perform additional actions like sending a confirmation email
            login(request, user)
            return redirect('home')  # Redirect to the home page
    else:
        form = UserRegistrationForm()

    context = {
        'page': page,
        'form': form,
    }
    return render(request, 'base/login-register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def userProfile(request, pk):
    user = MyUser.objects.get(id=pk)
    rooms = user.room_set.all()
    comments = user.comment_set.all()

    room_activities = [room.get_creation_activity() for room in rooms]
    comment_activities = [comment.get_activity() for comment in comments]

    activities = sorted(
        list(room_activities) + list(comment_activities),

        reverse=False
    )

    context = {
        'user': user,
        'rooms': rooms,
        'comments': comments,
        'activities': activities,
    }
    return render(request, 'base/profile.html', context)


def updateUser(request):
    pass


def home(request):
    movies_rooms = Room.objects.filter(room_type__name=Type.MOVIE)
    series_rooms = Room.objects.filter(room_type__name=Type.SERIES)
    category = Category.objects.all()[0:6]

    # gets the count of comments on each movie/series
    movies_rooms = movies_rooms.annotate(comment_count=Count('comment'))
    series_rooms = series_rooms.annotate(comment_count=Count('comment'))

    room_activities = []
    comment_activities = []

    created_rooms = Room.objects.all()
    comments = Comment.objects.all()  # Fetch comments by the logged-in user

    for room in created_rooms:
        room_activities.append(f"{room.host} created {room.name}")

    for comment in comments:
        comment_activities.append(f"{comment.user} commented on {comment.room}")

    context = {
        'movies_rooms': movies_rooms,
        'series_rooms': series_rooms,
        'category': category,
        'room_activities': room_activities,
        'comment_activities': comment_activities,
    }
    return render(request, 'base/home.html', context)


def room(request, pk):
    room_ins = Room.objects.get(id=pk)
    members = room_ins.participants.all()
    room_comments = room_ins.comment_set.all().order_by('-created')

    if request.method == 'POST':
        comment = Comment.objects.create(
            user=request.user,
            room=room_ins,
            body=request.POST.get('body'),
        )
        room_ins.participants.add(request.user)
        return redirect('room', pk=room_ins.id)

    context = {
        'room_ins': room_ins,
        'members': members,
        'room_comments': room_comments,
    }
    return render(request, 'base/room.html', context)


def createRoom(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            room.save()
            return redirect('home')  # Redirect to a view where you list all rooms
    else:
        form = RoomForm()
    context = {
        'form': form,
    }
    return render(request, 'base/room-form.html', context)


def updateRoom(request):
    pass


def deleteRoom(request):
    pass


# Message/Comments View

def deleteComment(request, pk):
    comment = Comment.objects.get(id=pk)
    if request.user != comment.user:
        return HttpResponse('You are not allowed to edit rooms.')

    if request.method == 'POST':
        comment.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': comment})
