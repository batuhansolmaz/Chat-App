"""home URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from products.viewsets import ProductViewSet
from chat import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('' , TemplateView.as_view(template_name='home.html') ,name="home"),
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('login/' , views.user_login ,  name='login' ),
    path('logout/' , views.user_logout ,  name='logout' ),
    path('signup/' , views.signup , name ='signup'),
    path('profile/' , views.ProfileDetail.as_view() , name ='profile'),
    path('create_room/' , views.create_room , name ='create_room'),
    path('profile/exit' , views.exit , name ='exit'),
    path('add_member/' , views.add_member , name ='add_member'),
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 