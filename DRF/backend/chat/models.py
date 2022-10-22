from datetime import datetime
from statistics import mode
from PIL import Image
import uuid
from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class room(models.Model):
    id=models.UUIDField(primary_key=True , default=uuid.uuid4)
    name = models.CharField(max_length=255, blank=True)
    
class ChatUser(models.Model):
    user=models.ForeignKey(User , related_name="chat_user" , verbose_name="kullanıcı", on_delete=models.CASCADE)
    room=models.ForeignKey(room , related_name="chat_users" , verbose_name="oda",on_delete=models.CASCADE)
    type = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.room.name

class message(models.Model):
    user = models.ForeignKey(User , related_name='message' , verbose_name='kullanıcı',on_delete=models.CASCADE)
    room = models.ForeignKey(room , related_name='messages' , verbose_name='oda', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='mesaj içeriği')
    created_date = models.DateTimeField(auto_now_add=True)

    def get_date(self):
        return str(self.created_date.hour) + ":" + str(self.created_date.minute)

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE) 
    image= models.ImageField(default= 'default.jpg' , upload_to = 'profile_pics' )
    last_activity = models.DateTimeField(default=datetime.now,blank=True)

    def get_last_activity(self):
        print(self.last_activity.strftime("%Y-%m-%d %H:%M:%S"))
        return str(self.last_activity.strftime("%Y-%m-%d %H:%M:%S"))

    def __str__(self):
        return f'{self.user.username} Profile'
    


    def save(self,*args,**kwargs) -> None:
        #super().save()
        print(kwargs)
        print(len(kwargs))
        if len(kwargs) ==0:
            super().save()

            img = Image.open(self.image.path)

            if img.height>300 or img.width>300:
                print(123)
                output_size=(300,300)
                img.thumbnail(output_size)
                img.save(self.image.path)
        
        else:
            img = Image.open(self.image.path)

            if img.height>300 or img.width>300:
                print(123)
                output_size=(300,300)
                img.thumbnail(output_size)
                img.save(self.image.path)