# importing Modules
import sys
from default import spy
import add_status as AS
import add_friend as AF


#start_chat() function
def start_chat():
    current_status_message=None

    #displaying menu of spy_chat
    while True:
        print('\nMENU\n1. Add Status\n2. Add Friend\n3. Send Message\n4. Read Message\n5. Open Chat\n6. Close\n')

        #input choice
        menu_choice=int(raw_input('Select Options from Menu\n'))
        if menu_choice==1:
            current_status_message=AS.add_status(current_status_message)
        elif menu_choice==2:
            AF.add_friend()
        elif menu_choice==3:
            pass
        elif menu_choice==4:
            pass
        elif menu_choice==5:
            pass
        elif menu_choice==6:
            break
        else:
            print('\nPlease enter a valid choice\n')

#printing welcome message
print ('Welcome to Spy_Chat\n')

#input profile choice
profile_choice=int(raw_input('Enter 1 to go with default profile or 2 to enter Details\n'))
if profile_choice==1:
    spy_name=spy['name']
    spy_rating=spy['rating']
    spy_salutation=spy['salutation']
    spy_age=spy['age']
elif profile_choice==2:
    spy_name=raw_input('Enter name of the spy\n')
    spy_rating=raw_input('Enter rating of the spy\n')
    spy_age=int(raw_input('Enter age of the spy\n'))
    spy_salutation=raw_input('Enter The salutation Mr. or Ms.\n')
else:
    print('Enter correct choice\n')
    sys.exit(0)

#validating Name and Age
if spy_name.isalpha() == False:
    print('Invalid Spy Name\n')
    sys.exit(0)
if spy_age<18:
    print('Invalid age\n')
    sys.exit(0)

#assgining stars according to ratings
if spy_rating=='A+' or spy_rating=='a+':
    stars=5
elif spy_rating=='A'or spy_rating=='a':
    stars=4
elif spy_rating=='B+'or spy_rating=='b+':
    stars=3
elif spy_rating=='B'or spy_rating=='b':
    stars=2
else:
    stars=1

#printing details of spy
print('\nWelcome %s%s.You are %d years old. Your rating is %d stars.\n'%(spy_salutation,spy_name,spy_age,stars))

#calling start_chat()
start_chat()
