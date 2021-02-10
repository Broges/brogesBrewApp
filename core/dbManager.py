'''This file handles all database related things. Connecting, returning information
and inserting information'''

import os #library to imported to clear the screen
import psycopg2  #library for postgreSQL to allow connection functionality
from core.peopleClass import Person, PersonObject
from core.drinkClass import Drink, DrinkObject
from core.utils import clearScreen

class DB:
    def __init__(self): #Constructor doesn't need any attributes therefore
        pass            #we pass the constructor

    def insert_db_person(self):
        connection = psycopg2.connect(host = "localhost",      #connects to the local database with correct credentials
                                    user = "postgres",      #superuser
                                    password = "x",
                                    database = "analysis",
                                    port = "5432")  #database is listening on this port

        newPerson = PersonObject.createNewPerson()    #calls function which creates new 'Person' object, and assigns to 'newPerson'
        value = newPerson.returnPersonProperties()  #calls function which breaks down the object in to readable strings
        
        try: #will attempt to run indented code

            with connection.cursor() as cursor: #cursor object is used to commuicate with the database
                sql = ("INSERT INTO people VALUES ('%s','%s','%s','%s','%s','%s');"%(value[0],value[1],value[2],value[3],value[4],value[5])) #sql query, inserts vals from readable string
                cursor.execute(sql) #executes the query on the database

        except Exception as e: #error handling - returns error to the user
            print("Error: %s" %(e))

        connection.commit() #pushes the changes made to the database
        connection.close() #closes the connection to the database
        print("Person data created & uploaded")
        clearScreen() #calls clear screen function - QoL function

    def insert_db_drinks(self):
        connection = psycopg2.connect(host = "localhost",                   #connects to the local database with correct credentials
                                    user = "postgres",
                                    password = "x",
                                    database = "analysis",
                                    port = "5432")

        newDrink = DrinkObject.createNewDrink()     #calls function which creates new 'Drink' object, and assigns to 'newDrink'
        value = newDrink.returnDrinkProperties() #calls function which breaks down the object in to readable strings
        
        try:

            with connection.cursor() as cursor:
                sql = ("INSERT INTO drinks VALUES ('%s','%s','%s','%s','%s');"%(value[0],value[1],value[2],value[3],value[4]))
                cursor.execute(sql) 

        except Exception as e:
            print("Error: %s" %(e))
        connection.commit()
        connection.close()
        #print("closed")
        print("Drink data created & uploaded")
        clearScreen()

    def print_db_person(self):
        os.system("cls")
        page_count=1
        connection = psycopg2.connect(host = "localhost",
                                    user = "postgres",
                                    password = "x",
                                    database = "analysis",
                                    port = "5432")                            
        try:

            with connection.cursor() as cursor:
                sqlQuery = "SELECT * FROM people;" #sql query that returns all data from 'people' table
                cursor.execute(sqlQuery)
                peopleRecords = cursor.fetchall() #grabs all the results returned from the query

                for row in peopleRecords: #iterates through all results, with row being a record
                    print("================================")
                    print("Name: %s" %(row[0]))
                    print("Age: %s" %(row[1]))
                    print("Gender: %s" %(row[2]))
                    print("Eye Colour: %s" %(row[3]))
                    print("Hair Colour: %s" %(row[4]))
                    print("Occupation: %s" %(row[5]))
                    print("================================")
                    print("(Person #%d out of %d)" %(page_count,len(peopleRecords)))
                    print("\n")
                    page_count+=1
                    clearScreen()

        except Exception as e:
            print("Error occured: %s" %(e))

        finally: #the last step which ALWAYS happens even if error occurs
            connection.close() #closes connection to database
            print("All users printed.")
            print("Connection Closed.")

        clearScreen()

    def print_db_drinks(self):
        os.system("cls")
        page_count=1 #var used to count how many of the drinks have been printed
        connection = psycopg2.connect(host = "localhost",   #connects to database with
                                    user = "postgres",      #correct credentials
                                    password = "x",
                                    database = "analysis",  #
                                    port = "5432")          #                 
        try:

            with connection.cursor() as cursor:
                sqlQuery = "SELECT * FROM drinks;"
                cursor.execute(sqlQuery)
                drinkRecords = cursor.fetchall()

                for row in drinkRecords:
                    if row[1] == True: #changes values from a boolean
                        r1 = "Yes"     #into a more user-friendly and 
                    else:              #readable 'Yes' or 'No'
                        r1 = "No"      #
                    if row[2] == True: #
                        r2 = "Yes"     #
                    else:              #
                        r2 = "No"      #
                        
                    print("================================")
                    print("Name: %s" %(row[0]))
                    print("Fizzy?: %s" %(r1))
                    print("Alcoholic?: %s" %(r2))
                    print("Colour: %s" %(row[3]))
                    print("Measurement: %s" %(row[4]))
                    print("================================")
                    print("(Drink #%d out of %d)" %(page_count,len(drinkRecords)))
                    print("\n")
                    page_count+=1
                    clearScreen()

        except Exception as e:
            print("Error occured: %s" %(e))
        finally:
            connection.close()
            print("All drinks printed.")
            print("Connection Closed.")
        clearScreen()

    def returnPeople(self):
        connection = psycopg2.connect(host = "localhost",
                                    user = "postgres",
                                    password = "x",
                                    database = "analysis",
                                    port = "5432")                            
        try:

            with connection.cursor() as cursor:
                sqlQuery = "SELECT * FROM people;" #sql query that returns all data from 'people' table
                cursor.execute(sqlQuery)
                peopleRecords = cursor.fetchall() #grabs all the results returned from the query

        except Exception as e:
            print("Error occured: %s" %(e))

        finally: #the last step which ALWAYS happens even if error occurs
            connection.close() #closes connection to database

        return peopleRecords

    def returnDrinks(self):
        connection = psycopg2.connect(host = "localhost",
                                    user = "postgres",
                                    password = "x",
                                    database = "analysis",
                                    port = "5432")                            
        try:

            with connection.cursor() as cursor:
                sqlQuery = "SELECT * FROM drinks;"
                cursor.execute(sqlQuery)
                drinkRecords = cursor.fetchall()

        except Exception as e:
            print("Error occured: %s" %(e))

        finally:
            connection.close()

        return drinkRecords

db = DB() #creates an instance of the DB object, called db. 
          #this is so we can call the object's methods with db.<method>