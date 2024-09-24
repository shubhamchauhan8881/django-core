from django import forms
from . import models


class AddForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(max_length=1000)

    def clean_title(self):
        title = self.cleaned_data['title']
        if(len(title)) < 10:
            raise forms.ValidationError("title must be at least 10 characters")
        return title    

    def save(self):
        data = self.cleaned_data
        p = models.DailyThoughts.objects.create(
            title = data["title"],
            content = data["content"],
         )
        return p