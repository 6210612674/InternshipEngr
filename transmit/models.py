from django.db import models
# Create your models here.


class Transmit_file(models.Model):
    file = models.FileField(blank=True)
    sender = models.CharField(max_length=50)
    receiver = models.CharField(max_length=50)
    date = models.DateTimeField()

    def __str__(self):
        return f"sender:{self.sender} sent {self.file} to receiver:{self.receiver} when {self.date}"
