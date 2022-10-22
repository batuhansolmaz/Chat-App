import re
from django.contrib.sessions.models import Session
import datetime
from django.utils.safestring import mark_safe

from django.core import serializers
from django.core.cache import cache
from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import ChatUser ,room , message ,Profile
from django.contrib.auth .decorators import login_required
from django.http import JsonResponse
# Create your views here.
import json
from .serializers import ChatSerializer , UserSerializer , ProfileSerializer, UserEditSerializer , MessageSerializer

from.forms import CreateUserForm
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


@login_required(login_url="login")
def index(request):
    print(Session.objects.filter(expire_date__gte = datetime.datetime.now()).count())
    users = User.objects.all().exclude(username=request.user)
    rooms = ChatUser.objects.filter(user=request.user).exclude(room__name ="")

    

    data=ChatSerializer(rooms , many=True).data
    data2=UserSerializer(users, many=True).data
    

    depo=[]
    depo2=[]
    print(data2)
    for i in users:
        
        print(i.is_active)
    for i in data:   
        
        depo.append(dict(i))
    
    for j in data2:
        depo2.append(dict(j))
    
    depo=json.dumps(depo)
    depo= json.loads(depo)
    print(depo)
    depo2=json.dumps(depo2)
    depo2= json.loads(depo2)
    
    #print(depo2[0])
    return render( request , 'index.html' , {'data':depo ,'data2' : depo2})



@login_required(login_url="login")
def chat_room(request ,room_name):
    oda = room.objects.get(id= room_name)
    messages = message.objects.filter(room=oda)

    kullanıcılar = ChatUser.objects.filter( room=oda)
    depo=[]
    for i in kullanıcılar:
        profile=i.user.profile
        print(profile.image)
        depo.append(profile)
    print(depo)
    chat= room.objects.filter(id=room_name)
    #return JsonResponse({'room_name' : room_name} ,status= 200)
    
    return render(request , 'chatroom.html' , {'a' : oda , 'messages' : messages ,  'depo' : depo})


def user_login(request):
    if request.method=='POST' :
        print(request.POST)
        username= request.POST.get('username','')
        password= request.POST.get('password','')
        user = authenticate(username=username , password=password)
        print(user)
        if user:
            login(request , user)
            return redirect("/")
    return render(request , 'login.html' )

def user_logout(request): 
    logout(request)
    return redirect("/")

@login_required(login_url="login")
def start_chat(request,users):
   
    return JsonResponse({'data' : users} ,status= 200)
    
    

@login_required(login_url="login")
def dms(request, *args , **kwargs):
    
    r=json.loads(request.body)
    print(r)
    User1=r['username']
    User2=request.user.username
    User1Id=r['usernameId']
    User2Id=request.user.id

    user1=User(username=User1 ,id =User1Id)
    user2=User(username=User2 ,id =User2Id )
    

    q1=ChatUser.objects.filter(user=user1 ,type='dm')
    q2=ChatUser.objects.filter(user= user2, type='dm')


    for i in q1:
        for j in q2:
            if (i.room == j.room):
                print(i.room)
                
                return JsonResponse({'data' : i.room.id, "user2" : User1Id} ,status= 200)

    
    newroom = room.objects.create()
    roomId= newroom.id
    ChatUser.objects.create(user= user1 , room=newroom , type= 'dm')
    ChatUser.objects.create(user= user2 , room=newroom , type= 'dm')

    return JsonResponse({'data' : roomId, "user2" : User1Id} ,status= 200)




def start_dms(request):
    print(request)
    print(request.GET)
    #messages = message.objects.filter(room=)
    
    Roomıd= request.GET.get('id', None)
    User2pk = request.GET.get('username', None)

    print(User2pk , ' aşkmsdşaşsdsa ' , type(Roomıd))
    #print(ChatUser.objects.filter(user= User2, room=Roomıd).first().user)
    user=User.objects.get(id=User2pk)
    User2name=User.objects.get(id=User2pk).username
    profil=Profile.objects.get(user=user)
    messages = message.objects.filter(room=Roomıd)
    # messages=serializers.serialize("json",messages)
    # messages= mark_safe(messages)
    data =MessageSerializer(messages , many=True).data
    depo=[]
    for i in data:  
        depo.append(dict(i))

    depo=json.dumps(depo)
    depo= json.loads(depo)

    print(depo)
    messages=depo
    



     
    return render(request , 'dms.html' , {'data' : Roomıd , "user2" : User2name , 'messages' :messages , 'profil' :profil})
 

def signup(request):

    form = CreateUserForm()
    if request.method == 'POST' :
        print(request.POST)
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        data= {'username' : username , "password1" :password1 , 'password2' : password2}

        form = CreateUserForm(request.POST)
        if form.is_valid():
            a=form.save()
            print(a)
            b=User.objects.get(username=a)
            print(a.id)
            print(b.id)
            Profile.objects.create(user=a)
            return redirect('login')
        else:
            print(form.error_messages)
    context = {'form' : form}
    return render(request , "signUp.html" , context)

# @login_required(login_url="login")
# def profile(request):
#     user = request.user
#     print(user)
#     data = UserSerializer(user).data
#     rooms=ChatUser.objects.filter(user=request.user).exclude(type='dm')
#     data2=ChatSerializer(rooms , many=True).data

#     depo=[]
#     for j in data2:
#         depo.append(dict(j))
    
#     depo=json.dumps(depo)
#     depo= json.loads(depo)
    
#     print(data2)
#     return render(request , 'profil.html' , {'data' : data , 'rooms':depo})


class ProfileDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profil.html'

    def get(self, request , **kwargs):
        print(kwargs)
        user = request.user
        if user.is_authenticated:
            print(user)
            data = UserSerializer(user)
            rooms=ChatUser.objects.filter(user=request.user).exclude(type='dm')
            data2=ChatSerializer(rooms , many=True).data
            

            return Response({'data' : data, 'rooms': data2})
        else:
            return redirect("login")

    def post(self, request):
        print(request.data)
        print(request.data.get('username'))
        print(request.POST)
        print(request.user.profile)
        if len(request.data.get('image'))!=0:
            serializer2= ProfileSerializer(request.user.profile,data={'user' : request.user.id , 'image' : request.data.get('image')})
        else:
            serializer2= ProfileSerializer(request.user.profile,data={'user' : request.user.id})

        serializer = UserEditSerializer(request.user ,request.data)
        
        rooms=ChatUser.objects.filter(user=request.user).exclude(type='dm')
        data2=ChatSerializer(rooms , many=True).data
        
        if not serializer.is_valid():
            print(1)
            return Response({'data': serializer, 'rooms': data2})
        if not serializer2.is_valid():
            print(212)
            print(serializer2.error_messages)
            print(serializer2.errors)
            return Response({'data': serializer2, 'rooms': data2})

        serializer.save()
        serializer2.save()

        print(User.objects.get(id=request.user.id))
        return redirect('profile')

def create_room(request):

    users = User.objects.all().exclude(username=request.user)
    data=UserSerializer(users, many=True).data
    if request.method =='POST':
        
        usersId=request.POST.getlist('users')
        group_name = request.POST.get('group-name')
        
        if (bool(re.match('[a-zA-Z\s]+$', group_name))) and len(usersId)>0:
            print('true')

            new_room=room.objects.create(name=group_name)
            for i in usersId:
                user=User.objects.get(id=i)
                
                newchat=ChatUser.objects.create(user=user , room=new_room )
               

            newchat=ChatUser.objects.create(user=request.user , room=new_room )

            
        else:
            print('false')
            return render(request , "create_room.html" ,{'data' : data} )

    
    return render(request , "create_room.html" ,{'data' : data} )

def exit(request):
    
    id=request.POST.get('id')
    user = request.user
    add=request.POST.get('add')
    print(request.session)
    if id != None:

        a=ChatUser.objects.get(room=id , user =user)

        UserNumber= ChatUser.objects.filter(room=id)
        print(UserNumber)
        if len(UserNumber)==1:
            a.delete()
            oda=room.objects.get(id = id)
            oda.delete()
        else:
            a.delete()
    else:
        request.session['add'] =add
        return redirect('add_member')
        
    return redirect('profile')



def add_member(request ,*args):
    add=request.session['add']
    
    CurrentRoom=room.objects.get(id = add)
    kullanıcılar=ChatUser.objects.filter(room=add)
    users= User.objects.all()
    users=list(users)
    
    for i in kullanıcılar:
        users.remove(User.objects.get(username=i.user , id=i.user.id))

    print(users)
    
    data=UserSerializer(users, many=True).data
    if request.method =='POST':
        
        usersId=request.POST.getlist('users')
        
        print(usersId)
        
        if len(usersId)>0:
            print('true')
        
            
            for i in usersId:
                user=User.objects.get(id=i)
                try :
                    ChatUser.objects.get(user=user , room=CurrentRoom )
                except:
                    print("yok")
                    newchat=ChatUser.objects.create(user=user , room=CurrentRoom )
               

            
    else:
        print('false')
        return render(request , "add_member.html" ,{'data' : data} )

    
    return render(request , "add_member.html" ,{'data' : data} )