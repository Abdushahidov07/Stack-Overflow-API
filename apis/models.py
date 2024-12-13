from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .meneger import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def __str__(self):
        return self.email
    

class Questions(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    question = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at= models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.title
    

class Answer(models.Model):
    question = models.ForeignKey(Questions, related_name='answers',on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    answer = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at= models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return f"{self.user.email}"