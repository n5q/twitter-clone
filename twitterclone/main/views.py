from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import models
from . import forms

# Create your views here.
def home(request) -> HttpResponse:
    posts = models.Post.objects.all().order_by("-date")
    if request.method == "POST":
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = models.Post()
            post.title = form.cleaned_data["title"]
            post.content = form.cleaned_data["content"]
            post.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("Invalid form")
    else:
        form = forms.PostForm()

    data = {
        "posts": posts,
        "postform": form
    }
    return render(request, "home.html", data)


def error_404_view(request, exception):
    return HttpResponse("<h1>Page not found</h1>", status=404)
