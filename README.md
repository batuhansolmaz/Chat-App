# ChatApp 
This Project is a web application in which you can chat with your firends and customize your profile page.

## The main page

![homepage](https://user-images.githubusercontent.com/108425372/197344765-cfbc1c8c-d6e2-41a3-8488-b660fba81620.png)
 
 There are signup, login, Profile and Chat buttons. You can go to specific pages from there
 
 ## The SignUp page
 
 ![singup](https://user-images.githubusercontent.com/108425372/197344978-05190b4d-77e7-4a7b-9be9-198413523454.png)

In the code I wrote this part with rest-framework.
One can not create user without username models restriction and password model restrictions. So you can't put a common password.

## The Login page

![newlogin](https://user-images.githubusercontent.com/108425372/197345570-b6f53596-5014-4053-a77e-54c15592354f.png)


You can login to system from here. But if you stay inactive for 2 minutes your session going to be ended. So you will need to login back.

## The Profile page

![Profil](https://user-images.githubusercontent.com/108425372/197345424-e4c14805-9ea2-45c7-b647-890b21dba7d4.png)

This part is the profile page you can upload your profile data will be serialized and update your infos.

## The AddMember
![AddNewMember](https://user-images.githubusercontent.com/108425372/197345690-b056807c-79a1-477d-befa-a8aba6d8df1b.png)

You can select and add these members to specific groups


## The Create New Group
![CreateNewGroup](https://user-images.githubusercontent.com/108425372/197345774-86909c5c-a2ab-471c-a78f-d93a92663c18.png)
You can create new group from here


## Chat
![Chat](https://user-images.githubusercontent.com/108425372/197345840-1ae8696b-e55a-4d99-9c49-2231f112d2dd.png)

There are users and groups. It shows you the groups that you joined. 

and there is search functionality
![Search2](https://user-images.githubusercontent.com/108425372/197345919-ecc80d6f-a2a7-483f-b6a3-61b0c68df4ee.png)

you can search names. It will be filtered with javascript.


## DM part
![dm](https://user-images.githubusercontent.com/108425372/197345989-3195098a-b96a-43d3-a75e-d2b5c36f6e48.png)
The backend code automatically creates a websocket connection and you can send messages without refreshing the page. All mesagges are stored in the database with its send time.


![Search](https://user-images.githubusercontent.com/108425372/197346022-3a89c7d6-4bf7-4cc9-8633-39fb80282082.png)
 You can also search messages in the chat. 

## Group part
![Group](https://user-images.githubusercontent.com/108425372/197346154-a7659836-9650-47ef-88b7-b517a4509bee.png)

It is same with dm but you send messages to multiple people from here. You can also see the users who is in the group.



## Lastly

The last activity time of user is stored in the database.
The messages is also stored in database.
Passwords are hashed one can not see or use it.
I uppdate last activity with middleware.
Profile is stored in database. 
I used restframework functions ,classes and serializers in this project.
I used Javascript in HTML too so thats why it shows HTML code percentage too much and javascript too less
