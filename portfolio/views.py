from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


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

def project_view(request):
    projects = Project.objects.all()  # Fetch all projects from the database
    return render(request, 'projects.html', {'projects': projects})


def search(request):
    query = request.GET.get('q', '')
    if query:
        results = Blog.objects.filter(
            title__icontains=query
        ) 
    else:
        results = Blog.objects.none()  # Return no results if query is empty

    return render(request, 'search_results.html', {'query': query, 'results': results})



