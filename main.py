import functions as func
import os

id = None
accounts = None

# Loop
while True:
    #Ask to chose beetween login and creating a new account
    ans = input("1. Login \n2. Create Account \n> ")
    
    #If login was chosen then ask for username and password
    if ans == "1":
        os.system("clear")
        username = input("Username: ")
        os.system("clear")
        password = input("Password: ")
        os.system("clear")
        #If username and password was correct then the ID for that user is returned
        id = func.login(username, password)
        #If id = None the loop will continue because the username or password was wrong
        if id == None:
            continue
        #If id has a value the loop will end
        else:
            break
    elif ans == "2":
        os.system("clear")
        username = input("Username: ")
        os.system("clear")
        password = input("Password: ")
        os.system("clear")
        func.create_account(username, password)
        print("account created")
        continue
    #if "1" or "2" wasn't typed in Retry! will be printed and the loop will continue and run again 
    else:
        print("\n Retry! \n")
        continue
#checks if id has a value then run a new loop for choosing the next options
if id != None:
    while True:
        ans = input("""1. See accounts
        2. New account
        > """)
        if ans == "1":
            accounts = func.get_account_details(id)
        os.system('clear')
        if accounts != None:
            for i in accounts:
                print("Name: " + i["Account_name"] + "\nBalance: " + i["Balance"] + " kr" + "\nRouting number: " + i["Routing"])
            break
        elif accounts == None:
            os.system('clear')
            print("No accounts")
            break
            
        

