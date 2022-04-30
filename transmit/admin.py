from django.contrib import admin
from .models import *


class Transmit_file_admin(admin.ModelAdmin):
    list_display = ("id", "file", "desc", "sender", "receiver", "date")


# Register your models here.
admin.site.register(Transmit_file, Transmit_file_admin)
