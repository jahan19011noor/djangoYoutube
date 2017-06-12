from django.conf.urls import url
from . import views
from django.contrib.auth.views import (

    ####### django built in functions   ########

    login, logout,              #This imports a default built login page#
    password_reset,             #Gives the user a form to enter their email then the submit redirects to password_reset_done#
    password_reset_done,        #Tells the user to check the email and click the associated link there#
    password_reset_confirm,     #This function renders the actual html template that gets sent to the email address#
    password_reset_complete     #This is the view which gets rendered on click the token link send to the email#
)

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}),  #This makes sure the login.html is rendered instead of the default page#
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$', password_reset, name='reset_password'),
    url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete, name='password_reset_complete')
]