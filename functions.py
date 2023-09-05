import json
import random
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
def create_account(username, password):
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
    with open("jsons/accounts.json", "r", encoding="utf-8") as fr:
        t1 = json.load(fr)
    for i in t1:
        if i["ID"] == ID:
            user = i
    user["Accounts"]

