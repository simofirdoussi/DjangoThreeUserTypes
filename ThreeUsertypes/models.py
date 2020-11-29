from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_type1 = models.BooleanField('type1', default=False)
    is_type2 = models.BooleanField('type2', default=False)
