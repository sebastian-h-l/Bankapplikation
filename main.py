import functions as func

id = None
accounts = None

# Loop
while True:
    func.login_menu()
    
#checks if id has a value then run a new loop for choosing the next options
if id != None:
    while True:
        ans = input("1. See accounts\n2. New account\n3. See history\n> ")
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
                        amount = input("How much: ")
                        func.withdraw(id, route_number, amount)
                        continue
                    elif ans == "3":
                        ans = input("1. Internal transfer\n2. External transfer\n> ")
                        if ans == "1":
                            amount = input("How much: ")
                            reaciving_route = input("Input recieving account route number: ")
                            func.internal_transfer(id, route_number, reaciving_route, amount)
                        elif ans == "2":
                            amount = input("How much: ")
                            reaciving_user = input("Input recieving user: ")
                            reaciving_route = input("Input recieving account route number: ")
                            func.external_transfer(id, reaciving_user, route_number, reaciving_route, amount)
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
        elif ans == "3":
            func.print_history(id)

            
        

