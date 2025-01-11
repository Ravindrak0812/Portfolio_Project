from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.views.decorators.csrf import csrf_exempt
from .models import Visitor


def home(request):
    return render(request, 'home.html')

@csrf_exempt
def handleblog(request):
    posts = Blog.objects.all()
    context = {"posts": posts}
    return render(request, 'handleblog.html', context)


def about(request):
    return render(request, 'about.html')


def assistance(request):
    return render(request, 'Asistance.html')

def certificates(request):
    return render(request, 'certificates.html')

def projects(request):
    return render(request, 'projects.html')


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



def visitor_count(request):
    count = Visitor.objects.count()
    return render(request, 'home.html', {'unique_visitors': count})
