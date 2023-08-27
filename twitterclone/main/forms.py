from django import forms
from . import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ["author", "content"]
        widgets = {
            "author": forms.TextInput(attrs={
                "class": "postform-title",
                "placeholder": " Username"
            }),
            "content": forms.Textarea(attrs={
                "class": "postform-content",
                "placeholder": " Content"
            })


        }
