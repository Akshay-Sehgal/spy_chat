import sys
import default
print ('Welcome to Spy_Chat\n')
choice=int(raw_input('Enter 1 to go with default profile or 2 to enter Details\n'))
if choice==1:
    spy_name=default.spy_name
    spy_rating=default.spy_rating
    spy_salutation=default.spy_salutation
    spy_age=default.spy_age
elif choice==2:
    spy_name=raw_input('Enter name of the spy\n')
    spy_rating=raw_input('Enter rating of the spy\n')
    spy_age=int(raw_input('Enter age of the spy\n'))
    spy_salutation=raw_input('Enter The salutation Mr. or Ms.\n')
else:
    print('Enter correct choice')
    sys.exit(0)
if spy_name.isalpha() == False:
    print('Invalid Spy Name')
    sys.exit(0)
if spy_age<18:
    print('Invalid age')
    sys.exit(0)
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
print('Welcome %s%s.You are %d years old. Your rating is %d stars.\n'%(spy_salutation,spy_name,spy_age,stars))
