from django.urls import path
from portfolio import views
from .views import chatbot_response
urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('blog', views.handleblog, name="blog"),
    path('assistance', views.assistance, name="assistance"),
    path('certificates', views.certificates, name="certificates"),
    path('projects', views.project_view, name='projects'),
    path('search', views.search, name='search'),
    path('chatbot/', chatbot_response, name='chatbot'),
]
