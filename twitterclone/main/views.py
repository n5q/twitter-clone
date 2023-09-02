from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import models
from . import forms
from . import sentiment

# Create your views here.
def home(request) -> HttpResponse:
    posts = models.Post.objects.all().order_by("-date")
    if request.method == "POST":
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = models.Post()
            post.author = form.cleaned_data["author"]
            post.content = form.cleaned_data["content"]
            post_sentiment = sentiment.Sentiment(post.content, 0.3)
            post.sentiment = post_sentiment.polarity
            post.reaction_emoji = post_sentiment.emoji
            post.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("Invalid form")
    else:
        form = forms.PostForm()

    data = {
        "posts": posts,
        "postform": form,
        "ReactForm": forms.ReactForm
    }
    return render(request, "home.html", data)


def error_404_view(request, exception):
    return HttpResponse("<h1>Page not found</h1>", status=404)

def react(request, post_id):
    if request.method == "POST":
        form = forms.ReactForm(request.POST)
        if form.is_valid():
            post = models.Post.objects.get(pk=post_id)
            post.reactions += 1
            post.save()
            return HttpResponseRedirect("/")
        else:
            print(form.cleaned_data,5)
            return HttpResponse("Invalid form")
    else:
        form = forms.ReactForm()
    return HttpResponseRedirect("/")