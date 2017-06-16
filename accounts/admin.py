from django.contrib import admin
from accounts.models import UserProfile

# one way of changing the admin page header
# admin.site.site_header = 'Administration'

# the other way is by making a html file in the templates/admin directory
    # which takes precedence over the default django admin page


# Creating a class to change the userProfile page of the admin

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'website', 'user_info', 'city',)

    # takes 1 argument

    def user_info(self, obj):

        # each row is an object in the database
        # runs through each of the rows of the description column
        # returns the description of the row

        return obj.description

    # get_queryset is inherited from ModelAdmin which has access to that
    # it is used to
        # get return from models
        # intercept the return from a model and
        # customize the return as well
    # so we need to
        # override the function ge_queryset but
        # also keep using its default features
            # to get the actual query result

    def get_queryset(self, request):

        # access teh get_queryset in the super class
            # access this class and then
            # access the super class's get_queryset
                # which this class has access to

        queryset = super(UserProfileAdmin, self).get_queryset(request)

        # then customize the order of the return

        queryset = queryset.order_by('-phone', 'user')

        return queryset

    # shorten name of the column user_info using .short_description

    user_info.short_description = 'Info'

# Register your models here.

admin.site.register(UserProfile, UserProfileAdmin)