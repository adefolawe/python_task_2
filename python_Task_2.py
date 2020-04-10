import random
import string
import re

def script():
            file=open("userinput.txt",'a+')

            while True:  
                first_n= input('First Name: ').capitalize()
                if not first_n.isalpha():
                    print("Your name must consist of letters only.")
                    continue
                else:
                    break
            while True: 
                last_n= input('Last Name: ').capitalize()
                if not last_n.isalpha():
                    print("Your name must consist of letters only.")
                    continue
                else:
                    break
               
            while True:
                email_add = input('Email Adress: ').lower()
                match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email_add)
                if match == None:
                    print('Invalid email address')
                    continue
          
                else:
                    break

            lists=first_n, last_n, email_add, ''
            for items in lists:
                file.write(items+"\n")

               
            def first_nString(length=2):
                return ''.join((random.choice(first_n) for i in range(length)))

            def last_nString(length=2):
                return ''.join((random.choice(last_n) for i in range(length)))


            def randString(length=5):
                letters= string.ascii_letters
                return ''.join((random.choice(letters) for i in range(length)))


            password_g = first_nString() + randString() + last_nString()
            password = password_g

            print ("Are you okay with this password", password)
            yn=input('(Y) or (N):' ).upper()
            if yn=='Y':
                print ('First Name:'+first_n,' ' 'Last Name:'+last_n, ' ' 'Email:'+email_add, ' ' 'Password:'+password)
            elif yn=='N':
                    while True:
                        password_n = input('Please input a password of 7 or more characters: ')
                        if len(password_n) < 7:
                            continue
                        
                        elif len(password_n) >= 7:
                            break
                    print ('First Name:'+first_n,' ' 'Last Name:'+last_n, ' ' 'Email:'+email_add, ' ' 'Password:'+password_n)

          
            _yn=input('Another user? (Y) or (N): ').upper()
            if _yn=='Y':
                script()

            elif _yn=='N':
                print('Thank you. Goodbye')
            breakpoint
script()
with open("userinput.txt") as f:
    print (f.read())
