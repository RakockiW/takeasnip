
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

from snippets.models import Snippet
from users.models import Profile


# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('snippet_list')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('snippet_list')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('snippet_list')

def user_profile(request):
    user = request.user
    profile = request.user.profile
    username = user.username
    xp = profile.xp
    rank = profile.rank
    snippets = Snippet.objects.filter(author=user.id)

    context = {
        'username': username,
        'xp' : xp,
        'rank' : rank,
        'snippets' : snippets,
    }

    return render(request, 'profile.html', context)