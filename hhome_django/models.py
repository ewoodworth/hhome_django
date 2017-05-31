from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

#https://stackoverflow.com/questions/4160770/when-should-i-use-ugettext-lazy
"""In definitions like forms or models you should use ugettext_lazy because the code of this definitions is only executed once (mostly on django's startup); ugettext_lazy translates the strings in a lazy fashion, which means, eg. every time you access the name of an attribute on a model the string will be newly translated-which makes totally sense because you might be looking at this model in different languages since django was started!

In views and similar function calls you can use ugettext without problems, because everytime the view is called ugettext will be newly executed, so you will always get the right translation fitting the request!
"""
class User(AbstractBaseUser):
    """
    Custom user class.
    """
    username = models.CharField( 'username', max_length=10, unique=True, db_index=True)
    email = models.EmailField('email address', unique=True)
    # name = 
    # lname = 
    # phone_number = 
    # avatar_src = 
    # address = 
    # chores = 
    # address = one to one with forwign table
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    
    def __repr__(self):
        """Provide helpful representation when printed."""
        return _("<User user_id=%s email=%s>") % (self.username.title(), self.email)

    def __str__(self):
        return self.username.title()

    def __unicode__(self):
        return self.username