from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm, EditProfileForm
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserChangeForm


def login(request):
    numbers = [1,2,3,4,5]
    name = "noor jahan mukammel"

    args = {'name':name, 'numbers':numbers}

    return render(request, 'accounts/login.html', args)

def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = RegistrationForm()

        args = {'form': form}

        return render(request, 'accounts/reg_form.html', args)

def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)


############### Code for Custome UserChange Form = EditProfileForm #################

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}

        return render(request, 'accounts/edit_profile.html', args)

############### Code for Custome UserChange Form = EditProfileForm #################


############### Code for Default UserChange Form #################

# from django.contrib.auth.forms import UserChangeForm

# def edit_profile(request):
#     if request.method == 'POST':
#         form = UserChangeForm(request.POST, instance=request.user)
#
#         if form.is_valid():
#             form.save()
#             return redirect('/account/profile')
#     else:
#         form = UserChangeForm(instance=request.user)
#         args = {'form': form}
#
#         return render(request, 'accounts/edit_profile.html', args)

############### Code for Default UserChange Form #################