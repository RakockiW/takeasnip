
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from snippets.models import Snippet
from users.forms import CustomLoginForm, CustomRegisterForm
from users.models import Profile


# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('snippet_list')
    else:
        form = CustomRegisterForm()

    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('snippet_list')
    else:
        form = CustomLoginForm()

    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('snippet_list')

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.profile
    username = user.username
    xp = profile.xp
    rank = profile.get_rank_display()
    snippets = Snippet.objects.filter(author=user.id)

    context = {
        'username': username,
        'xp' : xp,
        'rank' : rank,
        'snippets' : snippets,
    }

    return render(request, 'profile.html', context)