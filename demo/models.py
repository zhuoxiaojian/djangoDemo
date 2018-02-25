from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=20,blank=True)
    password = models.CharField(max_length=20,blank=True)
    
    
    def _str_(self):
        return self.username
    
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

class Entry(models.Model):
    blog = models.ForeignKey(Blog,on_delete=True)
    authors = models.ManyToManyField(Author)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()