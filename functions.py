import json
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
        
# def create_account(username, password):