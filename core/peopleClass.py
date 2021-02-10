'''This file handles the 'Person' class and its methods'''
from core.utils import clearScreen

class Person:
    def __init__(self,name,age,gender,eyeColour,hairColour,occupation):
        self.name = name                #constructor
        self.age = age                  #
        self.gender = gender            #
        self.eyeColour = eyeColour      #
        self.hairColour = hairColour    #
        self.occupation = occupation    #
    
    def returnPersonProperties(self):
        personProperties = self.name,self.age,self.gender,self.eyeColour,self.hairColour,self.occupation
        return personProperties #returns attributes of Person object in readable string

    def createNewPerson(self):
        nameInput=input("What is the person's name?: ")
        ageInput = int(input("What is the person's age?: "))
        genderInput = input("What is the person's gender?: ")
        eyeInput = input("What is the person's eye colour?: ")
        hairInput = input("What is the person's hair colour?: ")
        occInput = input("What is the person's occupation?: ")

        newPerson = Person(nameInput,ageInput,genderInput,eyeInput,hairInput,occInput)#creates new person
        clearScreen()
        return newPerson
        
PersonObject = Person("-","-","-","-","-","-")#Dummy Person object, used to call Person's methods