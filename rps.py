# Rock Paper Scissors Game

# import random
import quantumrandom

# ASCII Art
rpsart = []
rpsart.append('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

rpsart.append('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

rpsart.append('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

# item dictioary for mapping input to item
ditems = {"r":0, "p":1, "s":2}

# valid input
vinput = "rpsq"

# item list
plist = ["ROCK", "PAPER", "SCISSORS"]

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
  
  if userplay == '' or (not userplay in vinput):
    print("Invalid Input")
    print(game_instructions)
    continue
  elif userplay == "q":
    print("Goodbye!")
    break

  playindex = ditems[userplay]
  userplay = plist[playindex]
  print("\nYou chose " + userplay)
  print(rpsart[playindex])

  # rnd = random.randint(1,3) - 1
  rnd = int(quantumrandom.randint(1,3)) - 1
  cpu = plist[rnd]
  print("The computer chose " + cpu)
  print(rpsart[rnd])

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

