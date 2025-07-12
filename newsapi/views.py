import requests
from django.shortcuts import render, HttpResponse

def news_view(request):
    api_key = "36a29c69c34d47cbb24dd5199ab82aa7"  # Replace with your valid API key
    url = f"https://newsapi.org/v2/top-headlines?category=technology&apiKey={api_key}"


    # ✅ Use requests.get(url), NOT request.get(url)
    response = requests.get(url)  

    # # Debugging: Print API response in terminal
    # print(f"API Status: {response.status_code}")
    # print(f"API Response: {response.text}")

    if response.status_code != 200:
        return HttpResponse(f"Error fetching news: {response.status_code} - {response.text}")

    data = response.json()
    news_articles = data.get("articles", [])

    # If no articles found, return a message
    if not news_articles:
        return HttpResponse(f"No articles found. API Response: {data}")

    return render(request, "news.html", {"news": news_articles})
