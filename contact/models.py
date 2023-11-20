from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    Phone = models.CharField(max_length=30)
    message = models.TextField(max_length=30) 
  
  
  
    def _str_(self):
        return self.Name

class Booking(models.Model):
    Name = models.CharField(max_length=100)
    phone_Number = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    cab = models.CharField(max_length=100)
    Address = models.CharField(max_length=200)
    pinCode = models.CharField(max_length=10)
    Text = models.CharField(max_length=100)
    passengers = models.CharField(max_length=100)
    TimeStart = models.CharField(max_length=100)
    TimeEnd = models.CharField(max_length=100)
    comments = models.CharField(max_length=100)


    def __str__(self):
        return self.Name

class Booking2(models.Model):
    Name = models.CharField(max_length=100)
    phone_Number = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    cab = models.CharField(max_length=100)
    Address = models.CharField(max_length=200)
    pinCode = models.CharField(max_length=10)
    Text = models.CharField(max_length=100)
    passengers = models.CharField(max_length=100)
    TimeStart = models.CharField(max_length=100)
    TimeEnd = models.CharField(max_length=100)
    comments = models.CharField(max_length=100)
  
  
  
    def _str_(self):
        return self.Name