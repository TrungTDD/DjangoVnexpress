from django.core import paginator
from django.shortcuts import render
from .utils.util import parse_rss
from .models import SearchTopicForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    if request.method == "POST":
        form = SearchTopicForm(request.POST)
        if form.is_valid():
            rss_url = form.cleaned_data["rss_url"]
            news = parse_rss(rss_url)

            if news:
                return render(request, "vnexpress/index.html", {
                    "form": SearchTopicForm(),
                    "news" : news[:10]
                })
            else: 
                return render(request, "vnexpress/index.html", {
                    "form": SearchTopicForm(),
                    "news" : [],
                    "message" : "Wrong URL"
                })

    return render(request, "vnexpress/index.html", {
        "form": SearchTopicForm(),
        "news": [],
        "message" : "Enter URL"
    })

def error(request):
    return render(request, "vnexpress/error.html")
