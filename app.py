from core.menuSelect import app #Imports dummy object 'app', which is used to start the app

while True:        #Main loop of the program, user exists loop through menu option
    app.userMenu() #Brings up the choices the user has
    app.selector() #Takes input for the choices and calls relevant methods/functions