from django.shortcuts import redirect,render
from django.http import HttpResponse,HttpResponseRedirect
from purchase.models import Purchase
from django.core.mail import send_mail
from contactenquiry.models import contactEnquiry
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def booklib(request):
    return render(request,"booklib.html")
def contact(request):
    return render(request,"contact.html")
def saveEnquiry(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        en = contactEnquiry(name=name,email=email,message=message)
        en.save()
    return HttpResponseRedirect("/thankyou") 
    return render(request,"contact.html")
def purchase(request):
    return render(request,"purchase.html")
@csrf_protect
def purchase_view(request):
    if request.method == 'POST':
        book = request.POST.get('book')
        quantity = request.POST.get('quantity')
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        ps = Purchase(book=book,quantity=quantity,name=name,email=email,address=address)
        ps.save()
        send_mail(
            f"Helloo,{name}",
            "Your order is placed successfully,Thankyou !!",
            "daswanikhushbu10@gmail.com",
            [email],
            fail_silently=False
        )
        return render(request, 'success.html', {'name': name})
    return render(request, 'purchase.html')
def success(request):
    return render(request,"success.html")
def sign(request):
    return render(request,"sign.html")
def login(request):
    return render(request,"login.html")
def thankyou(request):
    return render(request,"thankyou.html")