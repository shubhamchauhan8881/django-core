from django.shortcuts import render, redirect
from . import models
from . import forms
from django.shortcuts import HttpResponse, HttpResponseRedirect



def home(req):
    # html (templates)  ->  render()
    all_thoughts = models.DailyThoughts.objects.all()  #-> QuerySet
    name = "shubham"
    return render(req, 'home.html' , context = {"thoughts": all_thoughts} )  #-> HttpResponse


def add(req):

    if req.method == "POST":
        f = forms.AddForm(req.POST)
        if f.is_valid():
            f.save()
            return redirect("homepage")
        else:
            return HttpResponse(str(f.errors))


    myForm = forms.AddForm()
    return render(req, 'add.html', context= {"MyForm": myForm} ) 
