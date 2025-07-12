from django.urls import path
from .views import news_view

urlpatterns = [
    path('api/news/', news_view, name='fetch_news'),
]
