from django.conf.urls import url
from home import views

urlpatterns = [
    # url for function-based view
    # url(r'^$', views.home, name='home')

    # url for class-based view
    # as_view() is a method in the TemplateView class
    # which has been inherited by the HomeView class
    # as_view() has be be passed because
        # url() function takes a function to get the template from
        # and as_view() returns that function
    url(r'^$', views.HomeView.as_view(), name='home')
]