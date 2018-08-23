"""
In this project, we'll build a basic calendar that the user will be able to interact with from the command line. The user should be able to choose to:

    View the calendar
    Add an event to the calendar
    Update an existing event
    Delete an existing event

The program should behave in the following way:

    Print a welcome message to the user
    Prompt the user to view, add, update, or delete an event on the calendar
    Depending on the user's input: view, add, update, or delete an event on the calendar
    The program should never terminate unless the user decides to exit

"""
from time import sleep, strftime
calendar = {}
def welcome():
  user = raw_input("Please Enter your user name: ")
  print "Welcome to your calendar " + user
  print "Calendar is opening...."
  sleep(1)
  print strftime("%A %m %d, %Y")
  print strftime("%H:%M:%S")
  sleep(1)
  print "What would you like to do?"

def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit: ").upper()
  
