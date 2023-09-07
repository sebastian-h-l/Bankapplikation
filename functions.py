import json
import random
import os

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
        else: # Kan nog ta bort else
            #Otherwise the loop will continue
            continue
    
    f.close()
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
    with open("jsons/credentials.json", "r", encoding="utf-8") as fr:
        t1 = json.load(fr)
    print(t1)

def get_account_details(ID):
    with open("jsons/accounts.json", "r", encoding="utf-8") as fr:
        t1 = json.load(fr)
    for i in t1:
        if i["ID"] == ID:
            print(i["Accounts"])
            return i["Accounts"]

def create_account(ID, accountname):
    user_excist = False
    account = {}
    account["Account_name"] = accountname
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

def internal_transfer(id, self_route, reciever_route, amount):
    with open("jsons/credentials.json", "r", encoding="utf-8") as fr:
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

    

def clear():
    os.system('cls||clear')