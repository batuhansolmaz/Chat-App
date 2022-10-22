
from asyncore import read
from requests import request
from rest_framework import serializers
from .models import ChatUser ,Profile ,message
from django.contrib.auth.models import User
import base64

from django.core.files.base import ContentFile

class   ChatSerializer(serializers.ModelSerializer):

    name =serializers.SerializerMethodField(read_only=True)
    type =serializers.SerializerMethodField(read_only=True)
    abc =serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model= ChatUser
        fields =[
            "user",
            "abc",
            "name",
            "type",
        ]


    def get_name(self,instance):
        
        return instance.room.name
    
    def get_type(self,instance):
        
        return 'group'
    
    def get_abc(self,instance):
        return str(instance.room.id)

class   UserSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(source='profile.image')
    last_activity=serializers.DateTimeField(source='profile.get_last_activity' , read_only=True)
    #password = serializers.CharField(write_only=True)
    
    class Meta:
        model= User
        fields =[
            "username",
            "id",
            'image',
            'last_activity'
            
        ]
    
   


   





class   UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields =[
            "username",
        ]
  
# class Base64ImageField(serializers.ImageField):
#     """
#     A Django REST framework field for handling image-uploads through raw post data.
#     It uses base64 for encoding and decoding the contents of the file.

#     Heavily based on
#     https://github.com/tomchristie/django-rest-framework/pull/1268

#     Updated for Django REST framework 3.
#     """

#     def to_internal_value(self, data):
#         from django.core.files.base import ContentFile
#         import base64
#         import six
#         import uuid

#         # Check if this is a base64 string
#         if isinstance(data, six.string_types):
#             # Check if the base64 string is in the "data:" format
#             if 'data:' in data and ';base64,' in data:
#                 # Break out the header from the base64 content
#                 header, data = data.split(';base64,')

#             # Try to decode the file. Return validation error if it fails.
#             try:
#                 decoded_file = base64.b64decode(data)
#             except TypeError:
#                 self.fail('invalid_image')

#             # Generate file name:
#             file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
#             # Get the file name extension:
#             file_extension = self.get_file_extension(file_name, decoded_file)

#             complete_file_name = "%s.%s" % (file_name, file_extension, )

#             data = ContentFile(decoded_file, name=complete_file_name)

#         return super(Base64ImageField, self).to_internal_value(data)

#     def get_file_extension(self, file_name, decoded_file):
#         import imghdr

#         extension = imghdr.what(file_name, decoded_file)
#         extension = "jpg" if extension == "jpeg" else extension

#         return extension


class  ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Profile
        fields =[
            'image',
            'user',
            'last_activity'
            
        ]
class MessageSerializer(serializers.ModelSerializer):
    user =serializers.SerializerMethodField()
    username=serializers.SerializerMethodField()
    room=serializers.SerializerMethodField()
    
    class Meta:
        model= message
        fields = ['content' , 'user' , 'room' ,'get_date','username']

    def get_user(self, instance):
        return instance.user.id
    def get_username(self, instance):
        return instance.user.username
    def get_room(self,instance):
        return str(instance.room.id)

    