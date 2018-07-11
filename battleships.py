from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
guess_row_input=input("Guess Row: ")
guess_col_input=input("Guess Col: ")
if type(guess_row_input) == int and type(guess_col_input) == int:
    guess_row = guess_row_input
    guess_col = guess_col_input
else:
    raise ValueError ("You need to use an Integer!")

if guess_row==ship_row and guess_col==ship_col:
  print ("Congratulations! You sank my battleship!")
else:
  if guess_row not in range(5) or \
  guess_col not in range(5):
    print ("Oops, that's not even in the ocean.")
  elif board[guess_row][guess_col] == "X":
    print ("You guessed that one already.")
    
  else:
    print ("You missed my battleship!")
    board[guess_row][guess_col] = "X"
    print_board(board)