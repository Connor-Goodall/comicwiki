from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .form import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
        return render(request, 'profile.html', {'u_form': u_form, 'p_form': p_form})

def users(request):
    owner = User.objects.filter(is_superuser = True)
    staff = User.objects.filter(is_staff = True)
    members = User.objects.exclude(is_staff = True)
    return render(request, 'users.html', {'owner': owner[0], 'staff': staff, 'members': members})

def profileInfo(request, username):
    user = User.objects.filter(username = username)
    return render(request, 'profileInfo.html', {'user': user[0]})

@login_required
def delete_confirm(request):
    return render(request, 'delete_account.html')

@login_required
def delete_done(request):
    user = request.user
    user.delete()
    return render(request, 'delete_account_done.html')
