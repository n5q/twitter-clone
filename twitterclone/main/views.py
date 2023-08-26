from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def home(request):
    posts = models.Post.objects.all()
    data = {
        "posts": posts
    }
    return render(request, "home.html", data)


def error_404_view(request, exception):
    return HttpResponse("<h1>Page not found</h1>", status=404)
