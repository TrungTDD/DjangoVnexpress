from os import name
from django.db import models
from django import forms
from django.db.models.fields import TextField

# Create your models here.

class SearchTopicForm(forms.Form):
    rss_url = forms.CharField(label="URL RSS")
