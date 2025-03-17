"""
URL configuration for museumgarden project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('lord-my-mh-admino/', admin.site.urls),
    path('', include('apps.main.urls', namespace='main')),
    path('places/', include('apps.places.urls', namespace='places')),
    path('blog/', include('apps.articles.urls', namespace='articles')),
    path('workshops/', include('apps.workshops.urls', namespace='workshops')),
    path('accounts/', include('apps.accounts.urls', namespace='accounts')),
    path('memories/', include('apps.memories.urls', namespace='memories')),
    
    path('gallery/', include('apps.gallery.urls', namespace='gallery')),
    path('personnel/', include('apps.personnel.urls', namespace='personnel')),
    
    path('search/', include('apps.search.urls', namespace='search')),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
handeler404='apps.main.views.handeler404'