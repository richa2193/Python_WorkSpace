from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegisterForm, UpdateProfileForm


# =========================
# REGISTER
# =========================

def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/patient/login/')

    else:

        form = RegisterForm()

    return render(request, 'patient/register.html', {'form': form})


# =========================
# LOGIN
# =========================

def user_login(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')

            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:

                login(request, user)

                return redirect('/patient/profile/')

    else:

        form = AuthenticationForm()

    return render(request, 'patient/login.html', {'form': form})


# =========================
# LOGOUT
# =========================

def user_logout(request):

    logout(request)

    return redirect('/patient/login/')


# =========================
# PROFILE UPDATE
# =========================

@login_required
def profile(request):

    if request.method == 'POST':

        form = UpdateProfileForm(request.POST, instance=request.user)

        if form.is_valid():

            form.save()

            return redirect('/patient/profile/')

    else:

        form = UpdateProfileForm(instance=request.user)

    return render(request, 'profile.html', {'form': form})