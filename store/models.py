from django.db import models

class Contacts(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Subject=models.CharField(max_length=100)
    Message=models.CharField(max_length=200)

 
 
 
    

    
 


 
    