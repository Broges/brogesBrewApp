'''This file handles the 'Preferences' class and its methods'''

from core.peopleClass import Person
from core.drinkClass import Drink
from core.utils import clearScreen
from core.dbManager import DB, db
preferences = [] #list of preferences, helps maintain consistency through runtime of app 

class Preferences: #creates a class called Preferences
    def __init__(self,name,drink):#constructor initalises the 
        self.name = name          #name and drink attributes
        self.drink = drink        #

    def createPreferences(self):
        global preferences #brings the global list in to the local scope
        personFlag = False #flag to recognise if the person has been identified
        drinkFlag = False #flag to recognise if the drink has been identified 
        allPeople = db.returnPeople() #calls method to get attributes of all people, assigns to var 'allPeople'
        allDrinks = db.returnDrinks() #calls method to get attributes of all drinks, assigns to var 'allDrinks'
        personInput = input("What is your name?: ")

        for peopleRow in allPeople: #iterates through all saved people
            if peopleRow[0] == personInput: #checks if the given name is found in the database
                personFlag = True #since name has been found, change flag to True
                drinkInput = input("What is your preffered drink?: ")

                for drinkRow in allDrinks: #iterates through all saved drinks
                    if drinkRow[0] == drinkInput: #checks if the given drink is in the database
                        drinkFlag = True
                        newPreference = Preferences(personInput,drinkInput)#creates preference object with given name and drink
                        preferences.append(newPreference)#adds the object to the global list
                        print("New preference added.")

        if personFlag == False:#checks if person was found
            print("You were not found on our system. Please register. ")

        if drinkFlag == False and personFlag == True: #checks if drink was found
            print("Drink is not in stock, sorry!")

        clearScreen()

    def printPreferences(self):
        global preferences

        for entry in preferences:#grabs names and drinks
            name = entry.name    #from each entry in 
            drink = entry.drink  #the preferences list
            print("%s's preffered drink is %s. \n"%(name,drink))

        clearScreen()
   
pref = Preferences("-","-") #creates dummy object to call the classes methods                 