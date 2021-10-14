from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.http import JsonResponse
from .models import Contacts
from django.core.mail import send_mail

# Create your views here.

def Home(response):
    if response.method=="POST":
        Name=response.POST["name"]
        Email=response.POST["email"]
        Subject=response.POST["subject"]
        message=response.POST["message"]

        send_mail(
           Name,#subject
           message,#message
           Email,#from email
           ["yawsarfo2019@gmail.com"] #to email,
            )

        Cont=Contacts.objects.create(Name=Name,Email=Email,Subject=Subject,Message=message)
        Cont.save()
        return redirect(New,name=Name)

        
    else:
        return render(response,"store/index.html",{})





def New(response,name):
    return render(response,"next.html",{"nameo":name})
        

         

       

        #The view store.views.Home didn't return an HttpResponse object. It returned None instead
   


   
   

        

       





         
   

