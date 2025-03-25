from django.db import models
from django.contrib.auth.models import AbstractUser


#### user
class User(AbstractUser):
    introduce = models.TextField()
