from django.db import models
from account.models import *
# Create your models here.


class Init_form(models.Model):
    file = models.FileField(blank=True)
    author = models.OneToOneField(Account, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f"Form:{self.file} was create by {self.author.user.username} when {self.date}"
