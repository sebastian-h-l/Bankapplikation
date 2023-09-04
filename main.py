import functions as func

ID = None

while True:
    ans = input("1. Login \n2. Create Account \n> ")
    
    if ans == "1":
        username = input("Username: ")
        password = input("Password: ")
        ID = func.login(username, password)
        if ID == None:
            continue
        else:
            break
    elif ans == "2":
        print("WIP")
        break
    else:
        print("\n Retry! \n")
        continue

if ID != None:
    while True:
        print("""1. See accounts
        2. See transaktions
        3. Send money
        4. Open new account""")
        ans = input("> ")
