############### Code for Custome Registration Form #################

from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm

def login(request):
    numbers = [1,2,3,4,5]
    name = "noor jahan mukammel"

    args = {'name':name, 'numbers':numbers}

    return render(request, 'accounts/login.html', args)

def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        # form = UserCreationForm()
        form = RegistrationForm()

        args = {'form': form}

        return render(request, 'accounts/reg_form.html', args)

############### Code for Custome Registration Form #################


############### Code for Default UserCreationForm #################

# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
#
# def login(request):
#     numbers = [1,2,3,4,5]
#     name = "noor jahan mukammel"
#
#     args = {'name':name, 'numbers':numbers}
#
#     return render(request, 'accounts/login.html', args)
#
# def home(request):
#     return render(request, 'accounts/home.html')
#
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/account')
#     else:
#         form = UserCreationForm()
#
#         args = {'form': form}
#
#         return render(request, 'accounts/reg_form.html', args)

############### Code for Default UserCreationForm #################