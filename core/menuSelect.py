'''This file handles the menus; it prints out the users options and
   calls the methods required when the relevant option is chose.
   Essentially this is the 'control tower'. '''
from core.roundClass import user_round
from core.dbManager import db
from core.preferenceClass import pref
from core.utils import clearScreen

class Selection():  #class to manage menu choices
    def __init__(self): #constructor is passed as only one instance of
        pass            #the class is required

    def selector(self):
        selection = input("\nEnter your selection here: ")
        print("\n")

        if selection == "1":
            db.print_db_person() #calls method which returns all people in database

        elif selection == "2":
            db.print_db_drinks() #calls method which returns all drinks in database

        elif selection == "3":
            db.insert_db_person() #calls method which inserts new person in database

        elif selection == "4":
            db.insert_db_drinks() #calls method which inserts new drink in database

        elif selection == "5":
            user_round.createRound() #calls method which creates a round

        elif selection == "6":
            user_round.isRoundActive() #calls method which checks if rounds are active

        elif selection == "7":
            pref.createPreferences() #calls method which creates a users preference

        elif selection == "8":
            pref.printPreferences() #calls method which prints users preferences

        elif selection == "9":
            exit() #exits the loop of printing user menu&selection, terminating the application
    
    def userMenu(self):
        print("Welcome to the Brew App! ")
        print("========================")
        print("\n[1] Output People Information")
        print("[2] Output Drink information")
        print("[3] Create New Person")
        print("[4] Create New Drink")
        print("[5] Create A Round")
        print("[6] Check Round Availability")
        print("[7] Create a preference")
        print("[8] Output saved preferences")
        print("[9] Exit")

app = Selection() #creates instance of Selection object called app
                  #this allows the methods to be called through app.<method>