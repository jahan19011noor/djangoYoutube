from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:         #Defines the meta data related to the class it is inside of#
        model = User   #Data will be stored in the User model#
        fields = (      #contains all the field in this form#
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):    #commit=True allows the data to be save on database#

        # prevents the save #
        user = super(RegistrationForm, self).save(commit=False)

        # prepare the fields for save #
        # cleaned_data works like http_real_escape_string #
        user.first_names = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User

        # We only need to exclude some of the code of the default UserChangeForm #
        # There are 2-ways to do this #

            # Using *fields #


        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        )

            # Using *exclude #

                # exclude = (fields that we want to exclude)