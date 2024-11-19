from django.db import models
from django.contrib.auth.models import User, PermissionsMixin, AbstractBaseUser, BaseUserManager
from PIL import Image

class UserProfileManager(BaseUserManager):
    
    def create_user(self, email, firs_tname, last_name, password):
        if not email:
            raise ValueError('User must have an email address...')

        email = self.normalize_email(email)
        user = self.model(email = email, first_name = firs_tname, last_name = last_name)
        user.set_password(password)
        user.save(using=self._db)

        return user 

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(email,first_name, last_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class Profile(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 255, unique = True, default = 'admin@sarc.org')
    role = models.CharField(max_length = 50, choices = [('Admin','Admin'),('Team Leader','Team Leader'),('User','User')], default = 'User')
    is_active = models.CharField(max_length = 3, choices = [('Yes', 'Yes'),('No','No')], default = 'Yes')
    is_staff = models.BooleanField(default = True)
   
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    objects = UserProfileManager()

    def __str__(self):
        return f'{self.email}'




