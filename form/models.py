from django.db import models
from Internship.settings import FORM_FILE_URL
from markdownx.models import MarkdownxField
from account.models import *
import os
# Create your models here.


class Init_form(models.Model):
    name = models.CharField(max_length=75)
    content = MarkdownxField()
    desc = models.CharField(max_length=300, blank=True, null=True)
    file = models.FileField(blank=True, upload_to=FORM_FILE_URL)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f"Form:{self.file} was create by {self.author.user.username} when {self.date}"

    def filename(self):
        return os.path.basename(self.file.name)
