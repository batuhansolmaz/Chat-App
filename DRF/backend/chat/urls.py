from .import views
from django.urls import path

urlpatterns = [
    path('', views.index , name= 'index'),
    
    path('dms/' , views.dms, name ='dms'),
    path('dms/start' , views.start_dms, name ='start_dms'),
    path('<str:room_name>/' , views.chat_room , name='room'),
    path('start_chat/<str:users>/' , views.start_chat , name ='start_chat'),
    
    


]