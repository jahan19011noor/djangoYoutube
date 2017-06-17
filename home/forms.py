from django import forms
from home.models import Post

class HomeForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a post..'
        }
    ))

    class Meta:
        model = Post

        # the comma says to unpack tuple and keep it as tuple and not transfer it to a string
        fields = ('post',)

#         Note:
#     we have not specified the User that has to be stored as well and that is not_empty by default
#     gives an error as request gets submitted because user_id does not get saved

#     We can save the user_id in the views.py

