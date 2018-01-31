from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=20,blank=True)
    password = models.CharField(max_length=20,blank=True)
    
    
    def _str_(self):
        return self.username