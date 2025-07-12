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



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Add to views.py
from django.core.cache import cache

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random


@csrf_exempt  # Remember to remove this in production
def chatbot_response(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '').lower()
            
            # Greetings
            if any(word in user_message for word in ['hello', 'hi', 'hey', 'hola']):
                response = random.choice([
                    "Hello! How can I assist you today?",
                    "Hi there! What would you like to know?",
                    "Greetings! How can I help with your questions?"
                ])
            
            # About the portfolio
            elif any(word in user_message for word in ['about', 'who are you', 'what is this']):
                response = "I'm an AI assistant for this portfolio. I can tell you about the projects, skills, and experience showcased here."
            
            # Projects
            elif any(word in user_message for word in ['project', 'work', 'portfolio']):
                response = random.choice([
                    "The portfolio includes several projects including web apps built with Django and React.",
                    "You'll find projects ranging from machine learning models to full-stack applications.",
                    "Check the projects section to see implementations using Python, JavaScript, and more."
                ])
            
            # Skills
            elif any(word in user_message for word in ['skill', 'technology', 'expertise']):
                response = "The technical skills demonstrated include Python, Django, JavaScript, React, SQL, and various data science libraries."
            
            # Experience
            elif any(word in user_message for word in ['experience', 'background', 'history']):
                response = "The portfolio showcases 3+ years of professional development experience across web development and data analysis."
            
            # Contact
            elif any(word in user_message for word in ['contact', 'email', 'reach', 'connect']):
                response = "You can find contact information in the contact section of this portfolio."
            
            # Availability
            elif any(word in user_message for word in ['hire', 'available', 'freelance', 'work']):
                response = random.choice([
                    "The portfolio owner is open to new opportunities. Check the contact section to get in touch.",
                    "For hiring inquiries, please use the contact information provided in the portfolio.",
                    "Availability details can be found in the contact section."
                ])
            
            # Education
            elif any(word in user_message for word in ['education', 'degree', 'school']):
                response = "The education section includes details about academic background and certifications."
            
            # Technical questions
            elif 'django' in user_message:
                response = "Django is used in several projects here as the backend framework for secure, scalable web applications."
            elif 'python' in user_message:
                response = "Python is the primary programming language used, particularly for web development and data analysis."
            elif 'javascript' in user_message:
                response = "JavaScript (and frameworks like React) are used for building interactive front-end applications in these projects."
            
            # Personal
            elif any(word in user_message for word in ['hobby', 'interest', 'passion']):
                response = "The portfolio highlights both professional work and personal interests in technology."
            
            # Fun responses
            elif any(word in user_message for word in ['joke', 'funny', 'laugh']):
                response = random.choice([
                    "Why do programmers prefer dark mode? Because light attracts bugs!",
                    "How many programmers does it take to change a light bulb? None, that's a hardware problem!"
                ])
            
            # Default intelligent response
            else:
                response = random.choice([
                    "I specialize in answering questions about this portfolio. Could you ask about the projects or skills?",
                    "That's an interesting question. Could you provide more details about what you'd like to know?",
                    "I'd be happy to help with portfolio-related questions. Try asking about the projects or experience.",
                    "I'm designed to discuss the content of this portfolio. Would you like to know about the projects or skills?"
                ])
            
            return JsonResponse({'response': response})
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)