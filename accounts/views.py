from django.shortcuts import render, redirect
from accounts.forms import (
    RegistrationForm,
    EditProfileForm
)
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm

# Used to update session after password change and ensure auto-login with new password #
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse

# To lock pages from unauthenticated users #
from django.contrib.auth.decorators import login_required


def login(request):
    numbers = [1,2,3,4,5]
    name = "noor jahan mukammel"

    args = {'name':name, 'numbers':numbers}

    return render(request, 'accounts/login.html', args)

# @login_required
# def home(request):
#     return render(request, 'accounts/home_old.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:home').lstrip('/'))
    else:
        form = RegistrationForm()

        args = {'form': form}

        return render(request, 'accounts/reg_form.html', args)


# @login_required
def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)

# @login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile').lstrip('/'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}

        return render(request, 'accounts/edit_profile.html', args)

# @login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            # Update the session #
                # User form.user = user who submitted the form, not the one who has been logged out on pass change #
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:view_profile').lstrip('/'))
        else:
            return redirect(reverse('accounts:change_password').lstrip('/'))

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}

        return render(request, 'accounts/change_password.html', args)