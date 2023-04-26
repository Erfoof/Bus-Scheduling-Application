def login():
    db = open("Users.txt", "r")
    username = input("Username: ")
    password = input("Password: ")
    u = []
    p = []
    for i in db:
        a,b = i.split(",")
        b = b.split()
        u.append(a)
        p.append(b)
    data =dict(zip(u, p))

    try:
        if data[username]:
            try:
                if password == data[username]:
                    print("login success")

                else:
                    print("Password or username incorrect")
            except:
                print("incorrect password of username")
        else:
            print("username does not exist")
    except:
        print("login error")
login()