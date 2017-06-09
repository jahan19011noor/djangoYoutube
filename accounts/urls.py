from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout     #This imports a default built login page#

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}),  #This makes sure the login.html is rendered instead of the default page#
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}),
    url(r'^register/$', views.register, name='register')
]