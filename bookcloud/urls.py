"""
URL configuration for bookcloud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from bookcloud import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('booklib/', views.booklib, name='booklib'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('purchase/', views.purchase, name='purchase'),
    path('sign-in/', views.sign, name='sign'),
    path('success/', views.success, name='success'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('saveenquiry/', views.saveEnquiry, name='saveEnquiry'),
    path('purchase_view/', views.purchase_view, name='purchase_view'),
]
