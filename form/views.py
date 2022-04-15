from tokenize import String
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template.defaultfilters import title
from django.urls import reverse
from django.contrib import messages

from account.models import Account
from .models import *
import datetime
from .forms import FormForm, MarkdownForm
import mimetypes
# use default_storage
from django.core.files.storage import default_storage
# Create your views here.


def index(request):
    form = Init_form.objects.all()
    return render(request, "form/index.html", {'form': form})


def create_initform(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Login First to proceed")
        return HttpResponseRedirect(reverse("account:index"))

    if request.method == "POST":
        name = request.POST["name"]
        desc = request.POST["desc"]
        file = request.FILES['form_file']
        content = MarkdownForm(request.POST)
        user = Account.objects.get(user=request.user)
        # Check name is already taken or not
        if Init_form.objects.filter(name=name).first():
            return render(request, 'form/create_initform.html', {
                "fail_name": "This name is already taken",
                "content": content
            })
        if content.is_valid():
            content = content.cleaned_data['Content']

            count = 0
            for x in Init_form.objects.all():
                count += 1
                filetype = file.name.split(".")[-1]
                time_now = datetime.datetime.now(datetime.timezone.utc)
                new_name = time_now.strftime(
                    "%d%m%y, %H%M%S") + "_" + str(count) + "." + filetype
                file.name = new_name

            new_form = Init_form.objects.create(
                name=name, content=content, file=file, author=user, desc=desc, date=datetime.datetime.now(datetime.timezone.utc))
            new_form.save()
            return HttpResponseRedirect(reverse("form:index"))
    else:
        content = MarkdownForm()
    return render(request, 'form/create_initform.html', {'content': content})


def download_file(request, file_id):
    form_field = Init_form.objects.get(id=file_id)
    # Set the return value of the HttpResponse
    response = HttpResponse(form_field.file)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % form_field.filename()
    # Return the response value
    return response


def form(request, id):
    form = Init_form.objects.get(id=id)
    return render(request, "form/form.html", {'form': form})


def delete_form(request, form_id):
    if not request.user.is_authenticated:
        messages.warning(request, "Login First to proceed")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    this_form = Init_form.objects.get(id=form_id)

    if request.user != this_form.author.user:
        return HttpResponseRedirect(reverse("form:form", args=(form_id,)))

    this_form.delete()
    return HttpResponseRedirect(reverse("form:index"))


def update_form(request, form_id):
    this_form = Init_form.objects.get(id=form_id)
    check_update = 1
    # Check user is own this form
    if request.user != this_form.author.user:
        return HttpResponseRedirect(reverse("form:form", args=(this_form.id,)))

    # If user submit update form
    if request.method == "POST":
        form = FormForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            content = form.cleaned_data['content']
            desc = request.POST["desc"]
            # Update  This form
            this_form.name = name
            this_form.content = content
            this_form.desc = desc
            this_form.save()

            return HttpResponseRedirect(reverse("form:form", args=(this_form.id,)))
    else:
        content = FormForm(request.POST or None, instance=this_form)

    return render(request, "form/form.html", {
        "form": this_form,
        "check_update": check_update,
        "form_update": content,
    })
