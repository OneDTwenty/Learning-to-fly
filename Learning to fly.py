#Learning to fly is my first attempt to relearn python since I haven't used this since 2014
#The code makes a login process and allows the user to execute commands
#There is an admin log for tracking actions, a user list, and a password file (this system is not ideal security)
#coded by Christian Helvie

#setting up date and time for stamping
import datetime

#open date and time mod
now = datetime.datetime.now()

#defining variables
tracker = 0
check = 0
name = ''

def main():

    command = input('What is your command (type list to see all commands)?\n')
    
    if command == 'blow up':
        print ('BOOM!!!')
        #erases all txt files used
        sys_log = open("Admin log.txt", "w+")
        sys_log.truncate()
        sys_log.close()       
        sys_log_user = open("Userlist.txt", "w+")
        sys_log_user.truncate()
        sys_log_user.close()
        sys_log_pass = open('Password.txt','w+')
        sys_log_pass.truncate()
        sys_log_pass.close()
        exit()
    elif command == 'exit':
        exit()
    elif command == 'restart':
        check = 0
        name = ''
        login(check,name)
    elif command == 'users':
        user_list = open('Userlist.txt','r')
        print(user_list.readline())
        user_list.close()
        main()
    elif command == 'list':
        print('**Command list**\r')
        print('blow up\r')
        print('exit\r')
        print('restart\r')
        print('users\n')
        print('list\n')
        main()

    print ('Invalid command\n')
    main()

def sys_track(tracker,name):

    #condition check
    if tracker == 1:
        sys_log = open("Admin log.txt", "a+")
        sys_log.write(f"\nFailed attempt by {name}")
        sys_log.write(now.strftime('%Y-%m-%d %H:%M:%S'))
        sys_log.close()
    else:
        #Welcome
        print (f'Welcome {name}.')

        #Time stamp login
        sys_log = open("Admin log.txt", "a+")
        sys_log.write(f"\nLoggin by {name}")
        sys_log.write(now.strftime('%Y-%m-%d %H:%M:%S'))
        sys_log.close()


def login(check,name):
        name = input('Username(type new for new user):\n')

        if name == 'new':
            newuser(name)

        password = input("Please enter your password:\n")

        for line in open("Password.txt","r").readlines():
            #login is split by username to password by a space
            login_info = line.split()
            if name == login_info[0] and password == login_info[1]:
                print("Correct credentials!")
                #call to log event
                tracker = 0
                sys_track(tracker,name)
                main()
                #return True
            
        print("Incorrect credentials.")
        tracker = 1
        sys_track(tracker,name)
        check = check + 1
        
        if check == 3:
            exit()
        else:
            login(check,name)

def newuser(name):
    #open files for edit
    sys_log_user = open("Userlist.txt", "a+")
    sys_log_pass = open("Password.txt", "a+")
    name = input('What is your new username?\n')

    # checks if user already exists
    for line in open("Password.txt","r").readlines():
        #login is split by username to password by a space
        login_info = line.split()
        if name == login_info[0]:
            print("This is already a user.")
            check = 0
            login(check,name)

    sys_log_user.write(f'{name}\n')

    password = input('What is your new password?\n')
    sys_log_pass.write(name)
    sys_log_pass.write(" ")
    sys_log_pass.write(password)
    sys_log_pass.write("\n")
    sys_log = open("Admin log.txt", "a+")
    sys_log.write(f"\nNew user created by {name}")
    sys_log.write(now.strftime('%Y-%m-%d %H:%M:%S'))

    sys_log_user.close()
    sys_log_pass.close()
    main()

#starts the login function
login(check,name)
