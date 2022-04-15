
from django.contrib import admin
from .models import *


class Init_form_admin(admin.ModelAdmin):
    list_display = ("name", "content", "desc", "file", "author", "date",)


# Register your models here.
admin.site.register(Init_form, Init_form_admin)
