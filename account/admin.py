from django.contrib import admin
from .models import *


class AccountAdmin(admin.ModelAdmin):
    list_display = ("user", "tel", "type",
                    "address", "year", "major", "current_state")
    filter_horizontal = ("sent_box", "read_box", "receive_box")


# Register your models here.
admin.site.register(Account, AccountAdmin)
