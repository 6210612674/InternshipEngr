from django.urls import path

from . import views

app_name = 'form'
urlpatterns = [path("", views.index, name="index"),
               path("create_initform", views.create_initform,
                    name="create_initform"),
               path('download_file/<int:file_id>',
                    views.download_file, name="download_file"),
               path('form/<int:id>',
                    views.form, name="form"),
               path("delete_form/<int:form_id>",
                    views.delete_form, name="delete_form"),
               path("update_form/<int:form_id>",
                    views.update_form, name="update_form"),
               path("internship/", views.internship, name="internship"),
               ]
