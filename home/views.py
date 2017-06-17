from django.shortcuts import render
from django.http import HttpResponse

# function-based view example:

# def home(request):
#     return HttpResponse('It Works')


# class-based view used:
    # import generic class-based view and
    # import TemplateView from there

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home/home.html'


# Note:
    # the TemplateView inherits from View class
        # the view class has the function called dispatch()
        # which extracts the method of the http request
            # and directs the request to the appropriate function
            # that has the same name as the method name
            # and contained in the child class
                # which is handling the request explicitely

    # thus comes the get(), post(), put() etc methods:
        # in the classes which are for the class-based views 