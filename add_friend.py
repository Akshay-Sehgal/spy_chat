friends=[]
#add_friend fucntion
def add_friend():

    friend = {
    'rating':raw_input('\nEnter Rating:\n'),
    'age':int(raw_input('\nEnter age of your:\n')),
    'name':raw_input('Enter the name of the user:\n'),
    'salutation':raw_input('\nEnter Salutation:\n')
    }



    if friend['name'].isalpha():
        if friend['age']>18 or friend['age']<40:
            friends.append(friend)
            print('FRIEND ADDED')


        else:
            print('Age  problem\n')
    else:
        print('Invalid Name \n')

    for i in range(0,len(friends)):
        print(friends[i])
