
def login(database, username, password):

    if username.casefold() in database and password == database[username]:
        print("welcome", username.casefold(), "!")
        return username
    if username.casefold() in database and not password == database[username]:
        print("Password is incorrect")
        return ""
    else:
        print("wrong username try again")
        return ""



def register(database, username):
    while True:


        if username.casefold() in database == database[username]:
            print("Username already registered.".casefold())
            return ""
        else:
            print(username.casefold(), "has been registered")
            return username.casefold()


