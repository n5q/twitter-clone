from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    reactions = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    author = models.CharField(max_length=50, default="")
    sentiment = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return self.title