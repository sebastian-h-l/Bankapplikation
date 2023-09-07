import json
import random
import os
from datetime import datetime

now = datetime.now()

def clear():
    os.system('cls||clear')

#Creates a function that checks if credentials match and then return id for the user
def login(username, password):
    #open credentials.json in read mode
    with open("jsons/credentials.json", "r", encoding="utf-8") as f:
        #Loads the json file into a variable
        t1 = json.load(f)
    #runs for loop checking if the username and password promted match with any user from the json file
    for i in t1:
        if i["Username"] == username and i["Password"] == password:
            #If it matches with a user that users id will be returned
            return i["ID"]
        
def create_user(username, password):
    user = {}         # Tom dictionary
    user["Username"] = username
    user["Password"] = password
    user["ID"] = str(random.randint(1000, 9999))
    with open("jsons/credentials.json", "r", encoding="utf-8") as fr:
        t1 = json.load(fr)
        t1.append(user)
    with open("jsons/credentials.json", "w", encoding="utf-8") as fw:
        json.dump(t1, fw)     
   
def login_menu():
    ans = input("1. Login \n2. Create Account \n> ")
    
    match ans:
        case "1":
            username = input("Username: ")
            clear()
            password = input("Password: ")
            clear()
            #If username and password was correct then the ID for that user is returned
            id = login(username, password)
            if id == None:
                login_menu()
        case "2":
            clear()
            username = input("Username: ")
            clear()
            password = input("Password: ")
            clear()
            create_user(username, password)
            print("New user created")
            login_menu()
        case _:
            clear()
            print("\n Retry! \n")
            login_menu()
    


def get_account_details(ID):
    with open("jsons/accounts.json", "r", encoding="utf-8") as fr:
        t1 = json.load(fr)
    for i in t1:
        if i["ID"] == ID:
            print(i["Accounts"])
            return i["Accounts"]

def create_account(ID):
    account_name = input("New accounts name: ")
    user_excist = False
    account = {}
    account["Account_name"] = account_name
    account["Balance"] = "1000.0"
    with open("jsons/accounts.json", "r", encoding="utf-8") as fr:
        t1 = json.load(fr)
    for i in t1:
        if i["ID"] == ID:
            user_excist = True
            amount = str(len(i["Accounts"]) + 1)
            if len(amount) < 3:
                amount = (3 - len(amount)) * '0' + amount
            account["Routing"] = amount
            i["Accounts"].append(account)
            with open("jsons/accounts.json", "w", encoding="utf-8") as fw:
                json.dump(t1, fw)
    if user_excist == False:
        user = {}
        user["ID"] = ID
        user["Accounts"] = [{"Account_name": accountname, "Balance": "1000.0", "Routing": "001"}]
        t1.append(user)
        with open("jsons/accounts.json", "w", encoding="utf-8") as fw:
            json.dump(t1, fw)

def second_menu():
    ans = input("1. See accounts\n2. New account\n3. See history\n> ")
    match ans:
        case "1":
            accounts = func.get_account_details(id)
            clear()
            if accounts != None:
                for i in accounts:
                    print("Name: " + i["Account_name"] + "\nBalance: " + i["Balance"] + " kr" + "\nRouting number: " + i["Routing"] + "\n")

def deposit(id, route, amount):
    with open("jsons/accounts.json", "r", encoding="utf-8") as fr:
        t1 = json.load(fr)
    for i in t1:
        if i["ID"] == id:
            for i in i["Accounts"]:
                if i["Routing"] == route:
                    i["Balance"] = str(float(i["Balance"]) + float(amount))
                    with open("jsons/accounts.json", "w", encoding="utf-8") as fw:
                        json.dump(t1, fw)
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    with open("jsons/transactions.json", "r", encoding="utf-8") as fr1:
                        t2 = json.load(fr1)
                    for i in t2:
                        if i["ID"] == id:
                            i["History"].append(f"Deposited {amount} kr to {route} at: {dt_string}")
                        with open("jsons/transactions.json", "w", encoding="utf-8") as fw1:
                            json.dump(t2, fw1)

                    
    
def withdraw(id, route, amount):
    with open("jsons/accounts.json", "r", encoding="utf-8") as fr:
        t1 = json.load(fr)
    for i in t1:
        if i["ID"] == id:
            for i in i["Accounts"]:
                if i["Routing"] == route:
                    i["Balance"] = str(float(i["Balance"]) - float(amount))
                    with open("jsons/accounts.json", "w", encoding="utf-8") as fw:
                        json.dump(t1, fw)
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    with open("jsons/transactions.json", "r", encoding="utf-8") as fr1:
                        t2 = json.load(fr1)
                    for i in t2:
                        if i["ID"] == id:
                            i["History"].append(f"Withdrew {amount} kr to {route} at: {dt_string}")
                        with open("jsons/transactions.json", "w", encoding="utf-8") as fw1:
                            json.dump(t2, fw1)

def display_users():
    with open("jsons/credentials.json", "r", encoding="utf-8") as fr:
        t1 = json.load(fr)
    for i in t1:
        print(i["Username"])


def external_transfer(id, reciever, self_route, reciever_route, amount):
    reciever_id = None
    with open("jsons/credentials.json", "r", encoding="utf-8") as fr:
        t1 = json.load(fr)
    for i in t1:
        if i["Username"] == reciever:
            reciever_id = i["ID"]
    with open("jsons/accounts.json", "r", encoding="utf-8") as fr:
        t1 = json.load(fr)
    for i in t1:
        if i["ID"] == id:
            for i in i["Accounts"]:
                if i["Routing"] == self_route:
                    i["Balance"] = str(float(i["Balance"]) - float(amount))
                    with open("jsons/accounts.json", "w", encoding="utf-8") as fw:
                        json.dump(t1, fw)
    with open("jsons/accounts.json", "r", encoding="utf-8") as fr:
        t1 = json.load(fr)
    for i in t1:
        if i["ID"] == reciever_id:
            for i in i["Accounts"]:
                if i["Routing"] == reciever_route:
                    i["Balance"] = str(float(i["Balance"]) + float(amount))
                    with open("jsons/accounts.json", "w", encoding="utf-8") as fw:
                        json.dump(t1, fw)
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    with open("jsons/transactions.json", "r", encoding="utf-8") as fr1:
        t2 = json.load(fr1)
    for i in t2:
        if i["ID"] == id:
            i["History"].append(f"Transfered {amount} kr to {reciever} : {reciever_route} at: {dt_string}")
        with open("jsons/transactions.json", "w", encoding="utf-8") as fw1:
            json.dump(t2, fw1)

def internal_transfer(id, self_route, reciever_route, amount):
    with open("jsons/accounts.json", "r", encoding="utf-8") as fr:
        t1 = json.load(fr)
    for i in t1:
        if i["ID"] == id:
            for i in i["Accounts"]:
                if i["Routing"] == self_route:
                    i["Balance"] = str(float(i["Balance"]) - float(amount))
                    with open("jsons/accounts.json", "w", encoding="utf-8") as fw:
                        json.dump(t1, fw)
    with open("jsons/accounts.json", "r", encoding="utf-8") as fr:
        t1 = json.load(fr)
    for i in t1:
        if i["ID"] == id:
            for i in i["Accounts"]:
                if i["Routing"] == reciever_route:
                    i["Balance"] = str(float(i["Balance"]) + float(amount))
                    with open("jsons/accounts.json", "w", encoding="utf-8") as fw:
                        json.dump(t1, fw)
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    with open("jsons/transactions.json", "r", encoding="utf-8") as fr1:
        t2 = json.load(fr1)
    for i in t2:
        if i["ID"] == id:
            i["History"].append(f"Transfered {amount} kr from {self_route} to {reciever_route} at: {dt_string}")
        with open("jsons/transactions.json", "w", encoding="utf-8") as fw1:
            json.dump(t2, fw1)

def print_history(id):
    with open("jsons/transactions.json", "r", encoding="utf-8") as fr:
        t1 = json.load(fr)
    for i in t1:
        if i["ID"] == id:
            os.system('cls||clear')
            print("History")
            for i in i["History"]:
                print(i)
    

