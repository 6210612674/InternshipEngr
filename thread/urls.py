from django.urls import path

from . import views

app_name = 'thread'
urlpatterns = [path("", views.index, name="index"),
               path("create_thread", views.create_thread, name="create_thread"),
               # Thread Page
               path("thread_page", views.thread_page, name="thread_page"),
               path("<int:thread_id>", views.thread, name="thread"),
               # Annoucement Page
               path("annoucement_page",
                    views.annoucement_page, name="annoucement_page"),
               path("<int:annoucement_id>", views.annoucement, name="annoucement"),
               path("delete_thread/<int:thread_id>",
                    views.delete_thread, name="delete_thread"),
               path("update/<int:thread_id>",
                    views.update_thread, name="update_thread"),
               ]
