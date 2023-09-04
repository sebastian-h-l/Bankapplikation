import functions as func

id = None

# Loop
while True:
    #Ask to chose beetween login and creating a new account
    ans = input("1. Login \n2. Create Account \n> ")
    
    #If login was chosen then ask for username and password
    if ans == "1":
        username = input("Username: ")
        password = input("Password: ")
        #If username and password was correct then the ID for that user is returned
        IndentationError = func.login(username, password)
        #If id = None the loop will continue because the username or password was wrong
        if id == None:
            continue
        #If id has a value the loop will end
        else:
            break
    elif ans == "2":
        print("WIP")
        break
    #if "1" or "2" wasn't typed in Retry! will be printed and the loop will continue and run again 
    else:
        print("\n Retry! \n")
        continue
#checks if id has a value then run a new loop for choosing the next options
if id != None:
    while True:
        print("""1. See accounts
        2. See transaktions
        3. Send money
        4. Open new account""")
        ans = input("> ")
