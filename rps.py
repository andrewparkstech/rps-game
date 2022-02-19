# Rock Paper Scissors Game

import random

# item dictioary for mapping input to item
ditems = {"p":0, "s":1, "r":2}

# valid input
vinput = "rpsq"

# item list
plist = ["PAPER", "SCISSORS", "ROCK"]

# constants
game_name = "Rock, Paper, Scissors"
game_instructions = "To make a play, type 'r', 'p', or 's'. 'q' to quit"
game_prompt = "Rock, Paper, or Scissors?"

# welcome to game
print("Welcome to " + game_name)
print(game_instructions)

# game loop
while True:
   # get and validate user input; break if 'q'
  userplay = input("\n" + game_prompt + "\n> ").lower()

  if not userplay in vinput:
    print("Invalid Input")
    print(game_instructions)
    continue
  elif userplay == "q":
    print("Goodbye!")
    break

  playindex = ditems[userplay]
  userplay = plist[playindex]
  print("\nYou chose " + userplay)

  rnd = random.randint(1,3) - 1
  cpu = plist[rnd]
  print("The computer chose " + cpu + "\n")

  if playindex == rnd:
    print("Draw.")
    continue

  if userplay == "ROCK":
    if cpu == "SCISSORS":
      print("Rock slams scissors. You WIN!")
    else:
      print("Paper covers rock. You LOSE.")
  elif userplay == "SCISSORS":
    if cpu == "PAPER":
      print("Scissors cut paper. You WIN!")
    else:
      print("Rock slams scissors. You LOSE.")
  else:
    # paper
    if cpu == "ROCK":
      print("Paper covers rock. You WIN!")
    else:
      print("Scissors cut paper. You LOSE.")


