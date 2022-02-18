# Rock Paper Scissors Game
objs = {"r":"ROCK", "p":"PAPER", "s":"SCISSORS"}
game_name = "Rock, Paper, Scissors"
game_instructions = "To make a play, type 'r', 'p', or 's'"
game_prompt = "Rock, Paper, or Scissors?"

print("Welcome to " + game_name)
print(game_instructions)
play = input(game_prompt + "\n> ")

print("You chose " + objs[play])

