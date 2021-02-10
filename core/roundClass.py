'''This file handles the 'Round' class and its methods. '''
from core.dbManager import DB, db
from core.utils import clearScreen

roundFlag = True

class Round:
    def __init__(self):
        pass

    def createRound(self):
        global roundFlag
        if roundFlag == False: #checks to see if rounds are being acceptd                                     
            print("We are currently not excepting rounds, sorry!")
            clearScreen()

        else:
            localFlag = True #flag to check if user is done adding to the round
            allPeople = db.returnPeople()#grabs all people info from database
            allDrinks = db.returnDrinks()#grabs all drink info from database
            roundNameList =[]#creates empty lists to be used later
            roundDrinkList =[]#

            while localFlag == True:
                personFlag = False#flags to confirm if name provided matches
                drinkFlag = False #data from database
                roundName = input("What is your name?: ")

                for peopleRow in allPeople:#iterates through all people data
                    if peopleRow[0] == roundName:#checks if person name matches input
                        personFlag = True#flag changes as name matched a data entry
                        roundNameList.append(roundName)
                        roundDrink = input("What drink do you want?: ")

                        for drinkRow in allDrinks:#checks if drink name matches input
                            if drinkRow[0] == roundDrink:
                                drinkFlag = True#flag changes as name matched a data entry
                                roundDrinkList.append(roundDrink)
                                userInput = input("\nDo you wish to enter more? Y/N: ")

                                if userInput == "Y":
                                    pass #method begins again from the start

                                else: 
                                    localFlag = False#method doesnt reiterate as flag is now false
                                    clearScreen()
                                    print("\nThis is your round: \n")
                                    for i in range(0,len(roundNameList)):
                                        print("%s has ordered a %s." %(roundNameList[i], roundDrinkList[i]))

                if personFlag == False or drinkFlag == False:
                    localFlag = False

            if personFlag == False:#person was not found
                print("You are not on our system. Please sign up.")
                localFlag = False#makes sure method doesnt reiterate and ends

            if drinkFlag == False and personFlag == True:#person was found, drink was not found
                print("That drink is not stocked, sorry!")
                localFlag = False#makes sure method doesnt reiterate and ends

            print("")            
            clearScreen()
    
    def isRoundActive(self):
        global roundFlag

        if roundFlag == True:
            print("Rounds are available!")
        else:
            print("Rounds are not available!")

        clearScreen()
        
user_round = Round() #creates dummy object, used to call the methods as user_round.<method>