from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save      #Will save the default django user object and run some code based on the post_save signal#

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)


#the kwargs contains a dic of key:value pairs#
#if the 'created' key is available#
    #the user_profile model is created#
        #the 'user' field values of which is obtained from the 'instance' key of the kwargs#
            #the 'instance' is the instance of the User object create already#
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


#We are connecting to the post_save signal#
#We are passing the create_profile function to it which will contain the block of code to be executed on the signal#
#The sender or initater of the signal is the User model which is built in to django#

post_save.connect(create_profile, sender=User)
