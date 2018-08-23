"""
In this project, we'll build Rock-Paper-Scissors!

The program should do the following:
- Prompt the user to select either Rock, Paper, or Scissors.
- Instruct the computer to randomly select either Rock, Paper, or Scissors.
- Compare the user's choice and the computer's choice.
- Determine a winner (the user or the computer).
- Inform the user who the winner is.
"""
from random import randint

options = ["Rock","Paper","Scissors"]
message = {"tie": "Yawn it's a tie!",
          "won" : "Yay you won!",
          "lost" : "Awww you lost..."}

def decide_winner(user_choice, computer_choice):
  print ("This is what you chose: %s" % user_choice)
  print ("This is what the computer chose: %s" % computer_choice)
  if user_choice == computer_choice:
    print (message["tie"])
  elif ( user_choice == options[0] and computer_choice == options[2] ) or (user_choice == options[1] and computer_choice == options[0]) or (user_choice == options[2] and computer_choice == options[1]):
    print (message["won"])
  else:
    print (message["lost"])

def play_RTS():
  user_choice = input("Enter Rock, Paper or Scissors: ").lower()
  computer_choice = options[randint(0,2)].lower()
  decide_winner(user_choice,computer_choice) 
  

    
play_RTS()