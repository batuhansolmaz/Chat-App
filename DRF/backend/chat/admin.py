from pyexpat import model
from queue import PriorityQueue
from django.contrib import admin

# Register your models here.
from .models import ChatUser, message , room , Profile

admin.site.register(room)
admin.site.register(Profile)

@admin.register(ChatUser)
class ChatUserAdmin(admin.ModelAdmin):
    list_display =["user" , "room"]
    class Meta:
        model=ChatUser

@admin.register(message)
class MessageAdmin(admin.ModelAdmin):
    list_display =["user" , "room" , "created_date"]
    class Meta:
        model=message