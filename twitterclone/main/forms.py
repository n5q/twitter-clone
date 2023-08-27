from django import forms
from . import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "postform-title",
                "placeholder": "Title"
            }),
            "content": forms.Textarea(attrs={
                "class": "postform-content",
                "placeholder": "Content"
            })
            

        }
