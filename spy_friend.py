from spy_class import Spy
from chat_class import Chat
import csv
from steganography.steganography import Steganography
from colorama import init
from colorama import Fore,Back
friends=[]

#add_friend fucntion
def add_friend():
    count=0
    name=raw_input('Enter Friend\'s name:\n')
    age=int(raw_input('\nEnter Friend\'s age:\n'))
    rating=raw_input('\nEnter Friend\'s Rating:\n')
    salutation=raw_input('\nEnter Friend\'s Salutation:\n')
    friend=Spy(name,age,rating,salutation)



    if friend.name.isalpha():
        if friend.age>18 or friend.age<40:
            friends.append(friend)
            write_friend=open('friends.csv','a')
            write=csv.writer(write_friend)
            write.writerow([friend.salutation,friend.name,friend.age,friend.rating])
            write_friend.close()
            print('FRIEND ADDED\n')


        else:
            print('Age  problem\n')
    else:
        print('Invalid Name \n')

    count_friend=open('friends.csv','r')
    read=csv.reader(count_friend)
    for row in read:
        count+=1
    count_friend.close()
    return count

def load_friend():
    names_list=[]
    count=0
    read_friend=open('friends.csv','r')
    read=csv.reader(read_friend)
    for row in read:
        count+=1
        print('%d. %s %s'%(count,row[0],row[1]))
        names_list.append(row[1])
    friend_choice=int(raw_input('Enter choice:\n'))
    name=names_list[friend_choice-1]
    return name

#SEND MESSAGE FUNCTION
def send_message():
    name=load_friend()
    text=raw_input('Enter message:\n')
    #special message
    if text.upper()=='SOS':
        print('HELP IS COMING YOUR WAY\n')
    chat=Chat(text,True,name)

    #STEGANOGRAPHY
    image=raw_input('Enter Name of the Image you want to encode!\n')
    output='o.jpg'
    Steganography.encode(image,output,text)
    print('Latest Message encoded\n')

    #Appending Message
    save_message=open('chats.csv','a')
    save_m=csv.writer(save_message)
    save_m.writerow([chat.friend_name,chat.message,chat.timestamp,chat.send_by_me])
    print('Message Sent and saved\n')


#READ MESSAGE FUNCTION WITH COLORS
def read_message():
    name=load_friend()
    read_message=open('chats.csv','r')
    read_m=csv.reader(read_message)
    #PRINTING CHAT TRANSCRIPT WITH DIFFERENT COLORS
    init()
    for row in read_m:
        if name==row[0]:
            print(Back.WHITE)
            print (Fore.RED+'%s'%(row[0])+Fore.BLACK+' %s'%(row[1])+Fore.BLUE+' %s'%(row[2]))
    print(Back.RESET+Fore.RESET)

    #STEGANOGRAPHY
    output=raw_input('\nEnter Name of the Image you want to decode!\n')
    message=Steganography.decode(output)
    print('Secret message: %s'%(message))
    if message.upper()=='SOS':
        print('HELP YOUR FRIEND RIGHT NOW\n')
