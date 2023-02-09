def show_homepage():
    print("      === DonateMe Homepage ===         ")
    print("---------------------------------------")
    print("| 1.   Login      | 2.   Register     |")
    print("---------------------------------------")
    print("| 3.   Donate     | 4. Show Donations |")
    print("---------------------------------------")
    print("|              5. Exit                |")
    print("---------------------------------------")
show_homepage()
def donate(username):


    donation_amt = int(input("Enter amount to donate: "))
    donation_string = (f"{username} Donated: ${int(donation_amt)}")
    print("thank you", donation_string)



    return donation_string

def show_donations(donations):
    print("\n--- All Donations ---")

    if donations == []:
        print("Currently, there are no donations.")
    else:
        print(donations, sep="\n")


