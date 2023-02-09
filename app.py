#from donations_pkg.user import register
from donations_pkg.homepage import show_homepage
from donations_pkg.user import login, register
from donations_pkg.homepage import donate
from donations_pkg.homepage import show_donations

database = {"admin": "password123",}
donations = []
authorized_user = ""
show_homepage()
total = 0

# if authorized_user == "":
#     print("You must be logged in to donate.")
# else:
#     print("Logged in as:", authorized_user)
############################################ input choices

while True:
    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as: ", authorized_user)

    user_choice = input("choose and option:")
    if user_choice == "1":
        username = input("enter your username: ".casefold())
        password = input("enter your password: ".casefold())
        authorized_user = login(database, username.casefold(), password)
        print("TODO: Write Login Functionality")
    if user_choice == "2":
         username = input("enter your username: ".casefold())
         if len(username) > 10:
             print("username cannot be over 10 characters")
             continue

         password = input("enter your password: ")
         if len(password) < 5:
             print("password must be at least 5 characters")
             continue

         authorized_user = register(database, username)
         if authorized_user != "":
             database[username] = password
# Donate functionality
    if user_choice == "3":
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)



# show Donation function

    if user_choice == "4":
        if authorized_user == "":
            print("You are not logged in.")
        else:
            show_donations(donations)
            print()



    elif user_choice == "5":
        print("leave Donation!")
        break
