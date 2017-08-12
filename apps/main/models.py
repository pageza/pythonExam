from __future__ import unicode_literals
import bcrypt
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validate_user(self,post):
        isValid = True
        if len(post.get('name')) < 2 :
            isValid = False
            #add a flash message
        if len(post.get('email')) < 5:
            isValid = False
            #add a flash message
        if len(post.get('password')) == 0 :
            isValid = False
            #add a flash message
        if post.get('password') != post.get('confPass'):
            isValid = False
            #add a flash message
        return isValid
    def log_in(self,post):
        user = self.filter(email=post.get('email')).first()
        if user and bcrypt.hashpw(post.get('password').encode(), user.password.encode()) == user.password:
            return (True, user)
        return (False, 'notuser')

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Quote(models.Model):
    author = models.CharField(max_length=255)
    quote = models.TextField()
    posted_by = models.ForeignKey(User, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
