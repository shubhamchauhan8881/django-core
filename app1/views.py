from django.shortcuts import render, redirect
from . import models
from . import forms
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views import View



# ======================= function based views =================
def home(req):
    # html (templates)  ->  render()
    all_thoughts = models.DailyThoughts.objects.all()  #-> QuerySet
    name = "shubham"
    return render(req, 'home.html' , context = {"thoughts": all_thoughts} )  #-> HttpResponse


def add(req):
    if req.method == "POST":
        submitted_form = forms.AddForm( req.POST )
        if submitted_form.is_valid():
            # save form data
            submitted_form.save_data()
            return redirect("homepage")
        else:
            return JsonResponse( submitted_form.errors )

    # get method
    myForm = forms.AddForm()
    return render(req, 'add.html', context= {"MyForm": myForm} ) 
# ============================ function based views end here ===========================



# ========================= class based view ==================================

class UserView(View):
    
    def post(self, req):
        submitted_form = forms.AddForm( req.POST )
        if submitted_form.is_valid():
            # save form data
            submitted_form.save_data()
            return redirect("homepage")
        else:
            return JsonResponse( submitted_form.errors )

    def get(self, req):
        myForm = forms.AddForm()
        return render(req, 'add.html', context= {"MyForm": myForm} ) 


# ========================= class based views end here =========================

# User, AnonomousUser