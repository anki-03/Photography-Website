from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from contact.models import Contact, Booking2
from contact.models import Booking


#from  contact.models import Contact
# Create your views here.
def index(request):
    return render(request,"pages/index.html")
    
def about(request):
    return render(request,"pages/about.html")
    
def contact(request):
    if request.method=='POST':
        contact=Contact(Name=request.POST['Name'], Email=request.POST['Email'], Phone=request.POST["Phone"], message=request.POST['message'])
        
        contact.save()
        return render(request, 'pages/index.html')
        #return HttpResponse('success')
    
    else:

        return render(request, 'pages/contact.html')
def Pricing(request):
    return render(request,"pages/Pricing.html")

def services(request):
    return render(request,"pages/services.html")
    
def Portrait(request):
    return render(request,"pages/Portrait.html")
        
def Wedding(request):
    return render(request,"pages/Wedding.html")
    
def Fashion(request):
    return render(request,"pages/Fashion.html")
  
def Baby(request):
    return render(request,"pages/Baby.html")
    
def maternity(request):
    return render(request,"pages/maternity.html")
    
def PreWedding(request):
    return render(request,"pages/PreWedding.html")
    
def video(request):
    return render(request,"pages/video.html")
    
def Booking(request):
   if request.method=='POST':
        booking=Booking2(Name=request.POST["NameBooking"],phone_Number=request.POST["phone_Number"],email=request.POST["email"],cab=request.POST["cab"],Address=request.POST["Address"],pinCode=request.POST["pinCode"],Text=request.POST["Text"],passengers=request.POST["passengers"],TimeStart=request.POST["TimeStart"],TimeEnd=request.POST["TimeEnd"],comments=request.POST["comments"])
       
        # booking = Booking(phone_Number = "once",Name = "once",email = "once",cab = "once",Address ="once",pinCode = "once",Text = "once",passengers = "once",TimeStart = "once",TimeEnd = "once",comments = "once")
        # contact=Booking2( Email='Email', Phone="Phone", message='message',Name="ajaja",)
        
        # contact.save()
        # Retrieve form data from the request
        booking.save()
        return render(request, 'pages/index.html')
        #return HttpResponse('success')
        
   else:

        return render(request, 'pages/Booking.html')
     