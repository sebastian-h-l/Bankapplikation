import json



def login(username, password):
    with open("jsons/credentials.json", "r", encoding="utf-8") as f:
        t1 = json.load(f)

    for i in t1:
        if i["Username"] == username and i["Password"] == password:
            return i["ID"]
        else:
            continue
        
# def create_account(username, password):