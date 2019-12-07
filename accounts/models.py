from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        ##username comes from built in User model 
        return "@{}".format(self.username)