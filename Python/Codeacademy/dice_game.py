from random import randint
from time import sleep

"""

Program that rolls a pair of dice and asks the user to guess the sum. 

"""
number_of_sides = 6

def check_guess(guess):
  if guess > max_val:
    print ("Guess is too high, guess again")
    guess = get_user_guess()
  elif guess <= 0:
    print ("Guess must be Valid")
    guess = get_user_guess()
  else:
    print ("Valid Guess, rolling...")
    rolled_val = roll_dice(number_of_sides)
    print (rolled_val)
    if guess == rolled_val:
      print ("You Win!!!")
    else:
      print ("Sorry, Try again...")
      
def get_user_guess():
  guess = int(input ("Enter a Guess: "))
  check_guess(guess)
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1,number_of_sides)
  sleep(1)
  print ("First Dice roll is: %i" %first_roll)
  second_roll = randint(1,number_of_sides)
  sleep(1)
  print ("Second Dice roll is: %i" %second_roll)
  sleep(1)
  total_roll = first_roll + second_roll
  print ("Total is: %i" %total_roll)
  return total_roll

max_val = number_of_sides * 2
print ("The max number is: %d" %(max_val))
guess = get_user_guess()
