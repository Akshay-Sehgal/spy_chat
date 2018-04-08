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
    count=0
    read_friend=open('friends.csv','r')
    read=csv.reader(read_friend)
    for row in read:
        count+=1
        print('%d. %s %s'%(count,row[0],row[1]))

#def load_chat():
#def save_chat():
def send_message():
    text=raw_input('Enter message:\n')
    image='E:\PYTHON+ML\spy_chat\\a.jpeg'
    output='o.jpg'
    Steganography.encode(image,output,text)



def read_message():
    output='o.jpg'
    message=Steganography.decode(output)
    print('Secret message: %s'%(message))
