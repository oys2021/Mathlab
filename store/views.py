from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.http import JsonResponse
from .models import Contacts

# Create your views here.

def Home(response):
    if response.method=="POST":
        Name=response.POST["name"]
        Email=response.POST["email"]
        Subject=response.POST["subject"]
        message=response.POST["message"]

        Cont=Contacts.objects.create(Name=Name,Email=Email,Subject=Subject,Message=message)
        Cont.save()

        
    else:
        return render(response,"store/index.html",{})
         

       

        #The view store.views.Home didn't return an HttpResponse object. It returned None instead
   


   
   

        

       





         
   

