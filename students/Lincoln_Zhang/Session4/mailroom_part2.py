#!/usr/bin/env python3

import sys,os,textwrap

print("Mailroom")

donors_db = {"Fred Flintstone":[100, 200, 50],
          "Barney Rubble":[100, 50, 600],
          "Wilma Flintstone":[1000, 50, 600, 200],
          "Pebbles Flintstone":[10, 5, 6]
          }


def Mail_to_donors(a_dict):
    """
    This Function is to generate Thank you letter to all donors in donors_db

    and store the letters in letters.txt file
    """
    with open ("letters.txt","w+") as f:
        for item in a_dict.items():
            name,amount = item
            amount = sum(amount)
            letter = textwrap.dedent("""
            Dear {},

            Thank you! The amount you donated is {}!

            Sincerely
            The Team

            """.format(name,amount))
            print(letter)
            f.write(letter)

def find_donor(name,cash):
    """
    This Function is to verify db with donor's name
    if this is the donor first donation, create a new record in donors_db
    otherwise, append this donation to donor's record list
    """
    if name in donors_db.keys():
        donors_db[name] = donors_db[name].append(cash)
    else:
        donation = []
        donor = {name:donation}
        donor[name].append(cash)
        donors_db.update(donor)
    return donor

def Thank_You():
    """
    This function is to generate thank you letter for each donation
    and store the letter by donor's name
    """
    donor_name = input("Please tell me your name: ")
    donation = input("Please tell me how much you would like to donate: ")
    find_donor(name = donor_name, cash = int(donation))
    print(donors_db)
    with open("{}.txt".format(donor_name),"w+") as f:

        letter = textwrap.dedent("""

        Thank you {}, 
        your generous donation amount is {}

        """.format(donor_name,donation))
        print(letter)
        f.write(letter)


def gen_stats(v):
    """
    this func is to process one donor's donation record
    return total amount, times of donation and average amount
    """
    total = sum(v)
    num = len(v)
    avg = format(total/num,".2f")
    return total, num, avg

def Report(a_dict):
    """
    this func is to print a table of donors_db to screen
    """
    header = "{:<20}  |{:^10}  |{:^10}  |{:>10}".format("Donor Name","Total Given","Num Gifts","Average Gift")
    print(header)
    for item in a_dict.items():
        k,v = item
        total, num, avg = gen_stats(v = v)
        row = "{:<20}  ${:^10}  {:^10}   ${:>10}".format(k,total,num,avg)
        print(row)

def Quit():
    sys.exit()

def main_menu():
    while True:
        answer = input(textwrap.dedent("""
        Choose an action:

        1 - Send a Thank You to a single donor.
        2 - Create a Report.
        3 - Send letters to all donors.
        4 - Quit
        >>>
            """))
        print("Your reply is ", answer)
        
        answer = answer.strip()
        if answer == "1":
            Thank_You()
        elif answer == "2":
            Report(a_dict=donors_db)
        elif answer == "3":
            Quit()
        else:
            print("Please input 1,2 or 3")

#main_menu()

if __name__ == "__main__":
    print("Welcome to mailroom!")
    main_menu()