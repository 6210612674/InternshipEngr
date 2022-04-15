from django import forms
from markdownx.fields import MarkdownxFormField
from form.models import Init_form


class MarkdownForm(forms.Form):
    Content = MarkdownxFormField()


class FormForm(forms.ModelForm):
    class Meta:
        model = Init_form
        fields = ['name', 'desc', 'content']
