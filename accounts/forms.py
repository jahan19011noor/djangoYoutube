from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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