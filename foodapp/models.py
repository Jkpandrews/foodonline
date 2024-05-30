from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('email is must')
        if not username:
            raise ValueError('username is must')

        user = self.model(
            email= self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username= username,
            password= password,
            first_name= first_name,
            last_name= last_name,
        )
        
        user.is_admin= True
        user.is_superadmin= True
        user.is_staff= True
        user.is_active= True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser):
    pass