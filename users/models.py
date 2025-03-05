from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  ROLES_CHOICES = [
    ('admin','Admin'),
    ('user', 'User')
  ]
  email = models.EmailField(unique=True)
  role = models.CharField(max_length=10 , choices= ROLES_CHOICES , default='user')
  def __str__(self):
    return f"{self.username} | {self.role}"
  