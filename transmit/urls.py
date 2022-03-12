from django.urls import path

from . import views

app_name = 'transmit'
urlpatterns = [path("", views.index, name="index")

               ]
