from django.db import models
from markdownx.models import MarkdownxField
from django.contrib.auth.models import User
# Create your models here.


class Thread(models.Model):
    header = models.CharField(max_length=300)
    content = MarkdownxField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.BooleanField(default=False)
    desc = models.CharField(max_length=300, blank=True, null=True)
    icon = models.ImageField(
        upload_to='static/thread/icon', blank=True, null=True)

    def __str__(self):
        return f"{self.header} by {self.author}"

    def search(self, search):
        if search.lower() in self.header.lower():
            return True
        return False

    class Meta:
        ordering = ['-date']
