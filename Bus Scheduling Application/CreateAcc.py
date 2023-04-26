import os
import pickle
enableCLS = False

def clear_screen():
    global enableCLS
    if enableCLS:
        print('screen_clear is ON!')
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            _ = os.system('cls')
    else:
        print('screen_clear disabled!')

def ClearScreenSetting():
    global enableCLS
    ch = input('\nDo you want to enable "Clear Screen"?\nPress Y for YES, any other keys for NO: ')
    if ch == 'Y' or ch == 'y':
        enableCLS = True
    else:
        enableCLS = False

if os.path.isfile('./Accounts') == False:
    Accounts = {}
    openfile = open("Accounts", "wb")
    pickle.dump(Accounts, openfile)
    openfile.close()
    
if os.path.isfile('./Users') == False:
    Users = {}
    openfile = open("Users", "wb")
    pickle.dump(Users, openfile)
    openfile.close()

def passcheck(password):
    x = 1 
    a,b,c,d = 0,0,0,0
    while (len(password)<8):
        print("Make sure your password is at least 8 letters long")
        password = input("Enter a password: ")
    else:
        for i in password: 
            if (i.islower()):
                a+=1            
            if (i.isupper()):
                b+=1            
            if (i.isdigit()):
                c+=1            
            if(i=='@'or i=='$' or i=='_' or i=='*' or i=='^' or i=='!' or i=='#'):
                d+=1
    if (a>=1 and b>=1 and c>=1 and d>=1 and a+b+c+d==len(password)):
        print("Valid Password")
    else:
        x = 0
        print("Invalid Password!")
        if a == 0:
            print("Please include a lowercase letter in your password.")
        elif b == 0:
            print("Please include a uppercase letter in your password.")
        elif c == 0:
            print("Please include a number in your password.")
        elif d == 0:
            print("Please include a special character in your password.")
    return x
        
def CreateAcc():
    ClearScreenSetting()
    Accounts = pickle.load(open("Accounts", "rb"))
    Users = pickle.load(open("Users", "rb"))
    print("Create a New Account")
    print("=====================")
    name = str(input("Enter your full name: "))
    age = int(input("Enter your age: "))
    town = str(input("Enter your town: "))
    clear_screen()
    print("Let's set your Account username and password")
    print("Make sure your username is at least 8 letters long.")
    user = input("Enter a username: ")
    for key in Accounts:
        while (user == key):
            print("Username already taken. Try Again")
            user = input("Enter a username: ")
    password = input("Enter a password: ")
    while passcheck(password) == 0:
        password = input("Enter a password: ")
    Accounts[user] = password
    pickle.dump(Accounts, open("Accounts", "wb"))
    Users[user] = [name, age, town]
    pickle.dump(Users, open("Users", "wb"))
    print(Accounts)
    print(Users)


CreateAcc()


        
        
        
        