import csv


#add_status() function
def add_status(current_status_message):

    if current_status_message==None:
        print('\nYou do not have a status Message\n')
    else:
        print('\nCurrent Status : %s\n'%current_status_message)
    status_choice=raw_input('\nDo you want to Select from Previously entered Status Message(s)\nEnter Y for YES and N for NO\n')
    if status_choice.upper()=='Y':
        count=0
        status=[]
        read_status=open('Status.csv','r')
        read=csv.reader(read_status)
        for row in read:
            count+=1
            print('%d.%s'%(count,row))
            status.append(row)

        read_status.close()
        status_message_choice=int(raw_input('\nEnter your choice\n'))
        current_status_message=status[status_message_choice-1]
        return current_status_message

    elif status_choice.upper()=='N':
        new_status_message=raw_input('\nEnter a new status message\n')
        if len(new_status_message)>0:
            current_status_message=new_status_message
            write_status=open('Status.csv','a')
            write=csv.writer(write_status)
            write.writerow([new_status_message])
            write_status.close()
            return current_status_message
        else:
            print('\nEnter Some Status\n')
    else:
        print('\nEnter from Y or N only!\n')
