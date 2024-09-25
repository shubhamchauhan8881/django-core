from django import forms
from . import models


class AddForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(max_length=1000)


    def clean_title(self):
        cleaned_title = self.cleaned_data["title"]

        if len(cleaned_title) > 100:
            raise forms.ValidationError("form title must be at least 100 characters")
        
        return cleaned_title

    
    def save_data(self):
        
        models.DailyThoughts.objects.create(
            title = self.cleaned_data["title"],
            content = self.cleaned_data["content"]
        )
