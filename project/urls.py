
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('portfolio.urls')),
    path('auth/', include('authapp.urls')),
    path('blog/', include('blog.urls')),  
    path('newsapi/', include('newsapi.urls')),  
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

