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
    url(r'^$', views.home, name='home'),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),  #This makes sure the login.html is rendered instead of the default page#
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),

    #the reset_password_done link is broken after adding the namespace#
    #because in the password_reset builf in function we have#
    #post_reset_redirect = reverse('password_reset_done')#
    #we need to have reverse('accounts:password_reset_done')#
    #we need to pass it as a parameter to the function#
    #giving the value of post_reset_redirect#

    url(r'^reset-password/$', password_reset,
        {'template_name': 'accounts/reset_password.html',
         'post_reset_redirect':'accounts:password_reset_done',
         'email_template_name':'accounts/reset_password_email.html'},
        name='reset_password'),

    url(r'^reset-password/done/$', password_reset_done,
        {'template_name':'accounts/reset_password_done.html'},
        name='password_reset_done'),

    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm,
        {'template_name': 'accounts/reset_password_confirm.html',
         'post_reset_redirect':'accounts:password_reset_complete'},
        name='password_reset_confirm'),

    url(r'^reset-password/complete/$', password_reset_complete,
        {'template_name': 'accounts/reset_password_complete.html'},
        name='password_reset_complete')
]