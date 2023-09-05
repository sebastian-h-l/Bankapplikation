import functions as func

id = None
accounts = None

# Loop
while True:
    #Ask to chose beetween login and creating a new account
    ans = input("1. Login \n2. Create Account \n> ")
    
    #If login was chosen then ask for username and password
    if ans == "1":
        func.clear()
        username = input("Username: ")
        func.clear()
        password = input("Password: ")
        func.clear()
        #If username and password was correct then the ID for that user is returned
        id = func.login(username, password)
        #If id = None the loop will continue because the username or password was wrong
        if id == None:
            continue
        #If id has a value the loop will end
        else:
            break
    elif ans == "2":
        func.clear()
        username = input("Username: ")
        func.clear()
        password = input("Password: ")
        func.clear()
        func.create_user(username, password)
        print("New user created")
        continue
    #if "1" or "2" wasn't typed in Retry! will be printed and the loop will continue and run again 
    else:
        print("\n Retry! \n")
        continue
#checks if id has a value then run a new loop for choosing the next options
if id != None:
    while True:
        ans = input("1. See accounts\n2. New account\n> ")
        if ans == "1":
            accounts = func.get_account_details(id)
            func.clear()
            if accounts != None:
                for i in accounts:
                    print("Name: " + i["Account_name"] + "\nBalance: " + i["Balance"] + " kr" + "\nRouting number: " + i["Routing"] + "\n")
                ans = input("1. Select account by routing number\n2. Back\n> ")
                if ans == "1":
                    route_number = input("Routing number: ")
                    ans = input("1. Deposit\n2. Withdraw\n3. Transfer\n> ")
                    if ans == "1":
                        amount = input("How much: ")
                        func.deposit(id, route_number, amount)
                        continue
                elif ans == "2":
                    continue
            elif accounts == None:
                func.clear()
                print("No accounts")
                continue
        if ans == "2":
            func.clear()
            account_name = input("Account name: ")
            func.create_account(id, account_name)
            continue

            
        

