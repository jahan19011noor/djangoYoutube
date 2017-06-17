from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.forms import HomeForm
from django.views.generic import TemplateView
from home.models import Post

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created')

        args = {'form':form, 'posts':posts}
        return render(request, self.template_name, args)

    def post(self, request):

        # request.POST populates the form with the data received via the request
        form = HomeForm(request.POST)

        if form.is_valid():
            # .save() associates the form with the model
            # as the Meta class says the model = Post
            # form.save()

            # rewrite .save() to save the user id
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['post']
            form = HomeForm()

            # redirects to the home page
            # thus recreates the csrf token
            # have to save data in database to display in this case.
            return redirect('home:home')

        # after redirect these line no longer load the data
            # the data now has to be picked up from database and
            # displayed using the get() method
        # args = {'form': form, 'text': text}
        # return render(request, self.template_name, args)

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