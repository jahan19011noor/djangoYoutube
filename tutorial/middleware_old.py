import re                                   #import regular expression#
from django.conf import settings            #Referencing the settings.py file#
from django.shortcuts import redirect       #redirect funciton imported#
from django.contrib.auth import logout

#re.compile:
    # Compile a regular expression pattern into a regular expression object,
    # which can be used for matching using its match() and search() methods#

#object list of compiled urls:
    # the LOGIN_URL is compiled
    # after the first / is removed by lstrip#

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]


#if settings has the attribute LOGIN_EXEMPT_URLS
    # itterate through them and
    # compile them and
    # add them to the list of EXEMPT_URLS#

if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]


#will illuminate the use of for example the repeated use of @login_required decorator#
class LoginRequiredMiddleware:

#'pass': Raises the error: TypeError: object() takes no parameters#
#because class requires construction: '__init__'#
#which requires 'instance' of class itself to be passed to it as 'self'#
    #   pass  #

    ######  so we have  **** explained ****   ######

    ######  get_response can be named anything but is required as it will be called by the middleware    ######
    def __init__(self, get_response):
        #so to make get_response callable#
        self.get_response = get_response

    ######  then define the call method using the __call__ method to call get response    ######
    def __call__(self, request):
        response = self.get_response(request)
        return response

#'process_view': will be called upon every request before every view load function in the views.py#
    #receives the view_load function as a parameter#
        #which might be 'view_profile' or 'edit_profile' so and so#

    ######  so we have  &&&& explained &&&&   ######
    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')     #checks if user is found in the request#

        #this causes to redirect far to many times because has the leading '/' of the url#
        # path = request.path_info

        #so we need to have#
        path = request.path_info.lstrip('/')

#---------      Problem     ---------#
#         we cannot logout because logout is in EXEMPT_URLS and cannot be accessed by logged in users
#         so have to log out users explicitely in the middleware before the is_authenticated check logic
#         so we have
        if path == 'account/logout/':
            logout(request)
#---------      Problem     ---------#

        #####   code rewrited below #####
        # if not request.user.is_authenticated():
        #     if not any(url.match(path) for url in EXEMPT_URLS):
        #         return redirect(settings.LOGIN_URL)
        #####   code rewrited below #####

        # rewriting the login to check the url and the to check is_authenticated():
        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)

        if request.user.is_authenticated and url_is_exempt:
            return redirect(settings.LOGIN_REDIRECT_URL)

        elif request.user.is_authenticated or url_is_exempt:
            return None

        else:
            return redirect(settings.LOGIN_URL)
        # rewriting the login to check the url and the to check is_authenticated():


#####-------Explanation--------#####

# **** explained **** #
# the middleware receives a function: 'get_response'
    # which will get the request as a parameter
    # and will be called upon each request
    # and the response will be returned#
# **** explained **** #

# &&&& explained &&&& #
# process_view is called by the get_response function
        # it checks if request has attribute user
        # if user is not authenticated
            # check if request url is in the object list of 'EXEMPT_URLS'
                # and thus redirects away from authentication protected pages
# &&&& explained &&&& #

# so
        # we write a function which will be called upon call the middleware
            # with the request that has been sent from the browser
        # we call it using the response variable in the __call__ method
            # the function in turn calls the process_view function
                # which excepts the view_func as parameter
                # and checks if request has attr user
                # then checks if user is authenticated
                # and then the rest

#####-------Explanation--------#####