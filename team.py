players = []

add_players = input("Would you like to add a player to the list? (Yes/No) ")

while add_players.capitalize() == "Yes":
  name = input("\nEnter the name of the player to add to the team: ")
  players.append(name)
  add_players = input("Would you like to add another player? (Yes/No) ") 

print(f"\nThere are {len(players)} players on the team.")

player_number = 1
for player in players:
  print(f"Player {player_number}: {player}")
  player_number += 1

keeper = int(input(f"Please select the goalkeeper by selecting the player number (1 - {len(players)}): "))

if keeper > 0:
  print(f"Great!!! The goalkeeper for the game will be {players[keeper - 1]}.")
