import functions as func

id = None

def transfer_menu(route):
    ans = input("1. Internal transfer\n2. External transfer\n> ")
    match ans:
        case "1":
            amount = input("How much: ")
            reaciving_route = input("Input recieving account route number: ")
            func.internal_transfer(id, route, reaciving_route, amount)
        case "2":
            amount = input("How much: ")
            func.display_users()
            reaciving_user = input("Input recieving user: ")
            reaciving_route = input("Input recieving account route number: ")
            func.external_transfer(id, reaciving_user, route, reaciving_route, amount)

def account_action(route):
    ans = input("1. Deposit\n2. Withdraw\n3. Transfer\n> ")
    match ans:
        case "1":
            amount = input("How much: ")
            func.deposit(id, route, amount)
            account_menu()
        case "2":
            amount = input("How much: ")
            func.withdraw(id, route, amount)
            account_menu()
        case "3":
            transfer_menu(route)
    

def account_menu():
    ans = input("1. Select account by routing number\n2. Back\n> ")
    match ans:
        case "1":
            route_number = input("Routing number: ")
            account_action(route_number)
        case "2":
            second_menu()

def second_menu():
    ans = input("1. See accounts\n2. New account\n3. See history\n> ")
    match ans:
        case "1":
            accounts_details = func.get_account_details(id)
            if accounts_details != None:
                for i in accounts_details:
                    print("Name: " + i["Account_name"] + "\nBalance: " + i["Balance"] + " kr" + "\nRouting number: " + i["Routing"] + "\n")
                account_menu()
            else:
                print("No accounts")
                second_menu()
        case "2":
            func.clear
            func.create_account(id)
            second_menu()
        case "3":
            func.print_history(id)
            second_menu()
        case _:
            func.clear()
            second_menu()

def login_menu():
    global id
    ans = input("1. Login \n2. Create Account \n> ")
    match ans:
        case "1":
            username = input("Username: ")
            func.clear()
            password = input("Password: ")
            func.clear()
            #If username and password was correct then the ID for that user is returned
            id = func.login(username, password)
            if id == None:
                login_menu()
            second_menu()
        case "2":
            func.clear()
            username = input("Username: ")
            func.clear()
            password = input("Password: ")
            func.clear()
            func.create_user(username, password)
            print("New user created")
            login_menu()
        case _:
            func.clear()
            print("\n Retry! \n")
            login_menu()

login_menu()