status_messages=[]

#add_status() function
def add_status(current_status_message):

    if current_status_message==None:
        print('\nYou do not have a status Message\n')
    else:
        print('\nCurrent Status : %s\n'%current_status_message)
    status_choice=raw_input('\nDo you want to Select from Previously entered Status Message(s)\nEnter Y for YES and N for NO\n')
    if status_choice.upper()=='Y':
        if len(status_messages)>0:
            for i in range (1,len(status_messages)+1):
                print('%d.%s'%(i,status_messages[i-1]))
            status_message_choice=int(raw_input('\nEnter your choice\n'))
            current_status_message=status_messages[status_message_choice-1]
            return current_status_message
        else:
            print('\nYou haven\'t entered any status before.\n')
    elif status_choice.upper()=='N':
        new_status_message=raw_input('\nEnter a new status message\n')
        if len(new_status_message)>0:
            current_status_message=new_status_message
            status_messages.append(current_status_message)
            return current_status_message
        else:
            print('\nEnter Some Status\n')
    else:
        print('\nEnter from Y or N only!\n')
