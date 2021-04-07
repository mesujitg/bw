"""FirstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from FirstProject import views, settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('', views.show_home, name='home'),
    path('about/', include('about.urls')),
    path('contacts/', include('contacts.urls')),
    path('courses/', include('courses.urls')),
    path('portfolio/', views.show_portfolio),
    path('subscribe/', views.do_subscribe, name='subscribe'),
    path('login/', views.do_login, name='login'),
    path('register/', views.do_register, name='register'),
    path('logout/', views.do_logout, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

