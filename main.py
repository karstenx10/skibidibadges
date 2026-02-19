import sys
import random
import time

badge_count = 0


def badge1():
  print("Congratulations, you have recieved the skibidi badge!")
  badge_name = "Skibidi Badge"
  badge_count + 1
  print(badge_name + "Has been added to your inventory") # for testing purposes


def start():
  print("Welcome to the Badge Simulator")
  print(f"-======================-")
  username = str(input("Please enter your username > "))
  print(f"Welcome {username}! Would you like to play a game?")
  print(f"""Choose a game to play:
  Diddy's Dih [ 1 ]
  The Tuller Family [ 2 ]
  """)
  time.sleep(.25)
  game_choice = int(input("> "))
  if game_choice == 1:
    print("You have chosen [ Diddy's Dih ]")
    time.sleep(.5)
    print("Rolling Die...")
    dice_roll = random.randint(1, 7)
    time.sleep(.5)
    print(f"You have rolled a {dice_roll}")
    if dice_roll >= 3:
      print("You have won!")
      badge1()
    elif dice_roll <= 3:
      print("You have lost.")
      time.sleep(1)
      print("Would you like to play again? y/n")
      go_again = str("> "))
      if go_again == "yes":
        # CONTINUE THIS
  elif game_choice == 2:
    print("You have chosen [ The Tuller Family ]")
    time.sleep(.5)
    print("Rolling Die...")
    dice_roll = random.randint(1, 7)
    time.sleep(.5)
    print(f"You have rolled a {dice_roll}")
    if dice_roll >= 4:
      print("You have won!")
      badge1()


start()
