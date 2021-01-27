from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

# User = get_user_model()

class RegisterModel(AbstractUser):
    email = models.EmailField(('email address'), unique=True)
    # num = models.IntegerField(('Phone number'))
    profileImage = models.ImageField(upload_to='pic',blank=True)
    is_block = models.BooleanField(default=False)

    # def get_absolute_url( self):
    #     return reverse('list')
