from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
# Create your views here.


def home(request):
    return render(request, 'home.html')


def handleblog(request):
    posts = Blog.objects.all()
    context = {"posts": posts}
    return render(request, 'handleblog.html', context)


def about(request):
    return render(request, 'about.html')


def assistance(request):
    return render(request, 'Asistance.html')


def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneno = request.POST.get('num')
        desc = request.POST.get('desc')
        query = Contact(name=name,email=email,phonenumber=phoneno,description=desc)
        query.save()

        messages.success(request, "Thanks for contacting Us. We will get by you soon..")
        return redirect('/contact')
    return render(request, 'contact.html')