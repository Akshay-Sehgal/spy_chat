# importing Modules
import sys
from spy_class import Spy
import add_status as AS
import spy_friend as SF
import csv

#LOAD CHAT WHEN APPLICATION STARTS
chats=[]
load_chats=open('chats.csv','r')
load=csv.reader(load_chats)
for row in load:
    chats.append(row)

#LOAD FRIENDS WHEN APPLICATION STARTS
friends=[]
load_friends=open('friends.csv','r')
load=csv.reader(load_friends)
for row in load:
    friends.append(row)


#start_chat() function
def start_chat():
    current_status_message=None
    friend_count=0

    #displaying menu of spy_chat
    while True:
        print('\nMENU\n1. Add Status\n2. Add Friend\n3. Send Message\n4. Read Message\n5. Close\n')

        #input choice
        menu_choice=int(raw_input('Select Options from Menu\n'))
        if menu_choice==1:
            spy.current_status_message=AS.add_status(spy.current_status_message)
            print('UPDATED STATUS MESSAGE : %s\n'%(spy.current_status_message))
        elif menu_choice==2:
            friend_count=SF.add_friend()
            print('No. Of Friends You have : %d\n'%(friend_count))
        elif menu_choice==3:
            SF.send_message()
        elif menu_choice==4:
            SF.read_message()
        elif menu_choice==5:
            break
        else:
            print('\nPlease enter a valid choice\n')

#printing welcome message
print ('Welcome to Spy_Chat\n')

#input profile choice
profile_choice=int(raw_input('Enter 1 to go with default profile or 2 to enter Details\n'))
if profile_choice==1:
    spy=Spy('PierceBrosnan',27,'A+','Mr.')
elif profile_choice==2:
    name=raw_input('Enter name of the spy\n')
    rating=raw_input('Enter rating of the spy\n')
    age=int(raw_input('Enter age of the spy\n'))
    salutation=raw_input('Enter The salutation Mr. or Ms.\n')
    spy=Spy(name,age,rating,salutation)
else:
    print('Enter correct choice\n')
    sys.exit(0)

#validating Name and Age
if spy.name.isalpha() == False:
    print('Invalid Spy Name\n')
    sys.exit(0)
if spy.age<18:
    print('Invalid age\n')
    sys.exit(0)

#assgining stars according to ratings
if spy.rating=='A+' or spy.rating=='a+':
    stars=5
elif spy.rating=='A'or spy.rating=='a':
    stars=4
elif spy.rating=='B+'or spy.rating=='b+':
    stars=3
elif spy.rating=='B'or spy.rating=='b':
    stars=2
else:
    stars=1

#printing details of spy
print('\nWelcome %s%s.You are %d years old. Your rating is %d stars.\n'%(spy.salutation,spy.name,spy.age,stars))

#calling start_chat()
start_chat()
