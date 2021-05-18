accounts ={"test" : "test1", "test2" : "password"}

username=input("please enter your username: ")
password=input("please enter the password for "+ username + ": ")

if(accounts.get(username) == password):
    print("login succesful")
    test=input(".")
else:
    print("wrong password")
