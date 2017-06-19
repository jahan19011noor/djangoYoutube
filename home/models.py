from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    post = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Friend(models.Model):
    friends = models.ManyToManyField(User)

    # in ManyToMany Relationship Django specifies a related name by default like
        # users = models.ManyToManyField(User, related_name='friend_set')
    # so for other assignments we need to provide custom related names
        # to differentiate from the default one

    current_user = models.ForeignKey(User, related_name='owner', null=True)

    @classmethod        #Means the method takes a class(cls) as a parameter rather than the instance(self) of a class#
    def make_friend(cls, current_user, new_friend):

##########          Explaining object, created = object.get_or_create()         ###########
        # A convenience method for looking up an object with the given kwargs
        # (may be empty if your model has defaults for all fields), creating one if necessary.

        # Returns a tuple of(object, created),
            # where object is the retrieved or created object
            # and created is a boolean specifying whether a new object was created.

        # This is meant as a shortcut to boilerplatish code.For example:
                # try:
                #     obj = Person.objects.get(first_name='John', last_name='Lennon')
                # except Person.DoesNotExist:
                #     obj = Person(first_name='John', last_name='Lennon', birthday=date(1940, 10, 9))
                #     obj.save()
        # which can be rewritten using get_or_create() like so:
##########          Explaining object, created = object.get_or_create()         ###########

        friend, created = cls.objects.get_or_create(
            current_user = current_user
        )

        friend.friends.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):

        friend, created = cls.objects.get_or_create(
            current_user = current_user
        )

        friend.friends.remove(new_friend)