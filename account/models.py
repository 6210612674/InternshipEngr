from django.db import models
from django.contrib.auth.models import User
from transmit.models import *
# Create your models here.


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tel = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    address = models.TextField(blank=True)
    year = models.CharField(max_length=2, blank=True)
    major = models.TextField(blank=True)
    sent_box = models.ManyToManyField(
        Transmit_file, related_name='%(class)s_sent_box', blank=True)
    read_box = models.ManyToManyField(
        Transmit_file, related_name='%(class)s_read_box', blank=True)
    receive_box = models.ManyToManyField(
        Transmit_file, related_name='%(class)s_receive_box', blank=True)
    current_state = models.IntegerField(default=0)

    def __str__(self):
        return f"user:{self.user.username} type:{self.type} name:{self.user.first_name} {self.user.last_name}"
