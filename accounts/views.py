from django.shortcuts import render, HttpResponse

def home(request):
    numbers = [1,2,3,4,5]
    name = "noor jahan mukammel"

    args = {'name':name, 'numbers':numbers}

    return render(request, 'accounts/home.html', args)