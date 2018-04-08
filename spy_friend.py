from spy_class import Spy
from chat_class import Chat
import csv
from steganography.steganography import Steganography

#add_friend fucntion
def add_friend():
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
            print('FRIEND ADDED\n')


        else:
            print('Age  problem\n')
    else:
        print('Invalid Name \n')


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

def send_message():
    name=load_friend()
    text=raw_input('Enter message:\n')
    chat=Chat(text,True,name)
    save_message=open('chats.csv','a')
    save_m=csv.writer(save_message)
    save_m.writerow([chat.friend_name,chat.message,chat.timestamp,chat.send_by_me])
    print('Message Sent and saved\n')
    #STEGANOGRAPHY
    image='E:\PYTHON+ML\spy_chat\\a.jpeg'
    output='o.jpg'
    Steganography.encode(image,output,text)
    print('Latest Message encoded\n')



def read_message():
    name=load_friend()
    read_message=open('chats.csv','r')
    read_m=csv.reader(read_message)
    for row in read_m:
        if name==row[0]:
            print('%s %s'%(row[1],row[2]))
    #STEGANOGRAPHY
    output='o.jpg'
    message=Steganography.decode(output)
    print('Secret message: %s'%(message))
