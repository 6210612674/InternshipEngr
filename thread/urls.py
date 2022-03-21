from django.urls import path

from . import views

app_name = 'thread'
urlpatterns = [path("", views.index, name="index"),
               path("create_thread", views.create_thread, name="create_thread"),
               path("<int:thread_id>", views.thread, name="thread"),
               path("delete_thread/<int:thread_id>",
                    views.delete_thread, name="delete_thread"),
               path("update/<int:thread_id>",
                    views.update_thread, name="update_thread"),
               ]
