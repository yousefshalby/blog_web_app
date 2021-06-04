from django.shortcuts import render, redirect
from .models import Profile
from .forms import UserUpateForm, RegistrationForm, ProfileUpdateForm
from  django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')

    else:
        form = RegistrationForm()

    return render(request, 'users/register.html', {'form':form}) 

@login_required
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    if request.method == "POST":
        user_form = UserUpateForm(request.POST, instance=request.user)
        prof_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid() :
            user_form.save()
            prof_form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('profile')

    else:
        user_form = UserUpateForm(instance=request.user)
        prof_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'u_form': user_form, 'p_form':prof_form}) 

