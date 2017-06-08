from django.conf.urls import url
from . import views
from django.contrib.auth.views import login     #This imports a default built login page#

urlpatterns = [
    url(r'^home/$', views.home),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}),  #This makes sure the login.html is rendered instead of the default page#
]