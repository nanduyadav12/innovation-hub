from django.shortcuts import render
from .models import ContactMessage
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
def shop(request):
    # Your shop view logic here
    return render(request, 'shop.html')
def about(request):
    # Your shop view logic here
    return render(request, 'about.html')
def services(request):
    # Your shop view logic here
    return render(request, 'services.html')
def contact(request):
    # Your shop view logic here
    return render(request, 'contact.html')
def blog(request):
    # Your shop view logic here
    return render(request, 'blog.html')
def cart(request):
    # Your shop view logic here
    return render(request, 'cart.html')
def thankyou(request):
    # Your shop view logic here
    return render(request, 'thankyou.html')
def checkout(request):
    # Your shop view logic here
    return render(request, 'checkout.html')
def contact_form(request):
     if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        message = request.POST['message']

        dc = contact_form.objects.filter(email=email).exists()
        print(dc)
        if dc==True:
            msg="Details already Exist"
            return render(request,contact.html)
        else:

         dc(fname=fname,lname=lname,email=email,message=message)
         dc.save()


       
     return HttpResponse("Form data saved successfully!")
        
        
       
        
     return render(request, 'contact.html')  #