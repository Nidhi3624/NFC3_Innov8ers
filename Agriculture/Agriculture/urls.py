"""
URL configuration for Agriculture project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views

from AgriApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage,name="homepage"),
    path('dash/',views.dashboard1,name="dash1"),
    path('predicts',views.predict,name="predict"),
    path('chat/',views.chat,name="chat"),
    path('disease-predict/', views.disease_prediction, name='disease_prediction'),
    path('weather/dashboard/',views.weather_dashboard,name="dashboard"),
    path('fertilizer/',views.predict12,name = "fertilizer"),
    path('chat12/',views.chat12,name="chat12"),
    path('signup/', views.signup, name='signup'),
    path('login/',views.login_view,name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)