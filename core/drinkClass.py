'''This file handles the 'Drink' class and its methods'''
from core.utils import clearScreen

class Drink: #creates an object called 'Drink'
    def __init__(self,name,isFizzy,isAlcholic,colour,measurement):#
        self.name = name            # constructor
        self.isFizzy=isFizzy        #
        self.isAlcholic=isAlcholic  #
        self.colour=colour          #
        self.measurement=measurement#
    
    def returnDrinkProperties(self):
        drinkProperties = self.name,self.isFizzy,self.isAlcholic,self.colour, self.measurement
        return drinkProperties #when the method is called, it will return the objects
                               #attributes in a readable string
    def createNewDrink(self):
        nameInput=input("What is the drink called?: ")

        fizzyInput = input("Is the drink fizzy? Y/N?: ")#changes output from "Y"
        if fizzyInput == "Y":                           #or "N"  to Boolean
            fizzyInput = True                           #
        else:                                           #True or False is more
            fizzyInput = False                          #readable to user

        alcoholInput = input("Is the drink alcholic? Y/N: ")#changes output from "Y"
        if alcoholInput == "Y":                             #or "N" to Boolean
            alcoholInput = True                             #
        else:                                               #True or False is more
            alcoholInput = False                            #readable to user

        colourInput = input("What is the drinks's colour?: ")
        measureInput = input("What is the measure of the drink?: ")
        newDrink = Drink(nameInput,fizzyInput,alcoholInput,colourInput,measureInput)
        clearScreen()
        return newDrink

DrinkObject = Drink("-","-","-","-","-")#Dummy drink object used to call Drink methods


