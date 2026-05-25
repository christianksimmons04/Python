# Written by Christian Simmons
# Hide and Seek

# Import modules
import time
import random

# Setting integer variables
countdown = 11
seeking_time = 0

# Starting the game
print("===Enter the Number===\n")

print("[1] Couch | [2] Curtain | [3] Shower\n")

user_option = input("Pick a hiding spot!\n")

# Options
if user_option == 1:
    print("[You chose the couch!]\n")
elif user_option == 2:
    print("[You chose the curtain!]\n")
elif user_option == 3:
    print("[You chose the shower!]\n")
else:
    print("Invalid integer chosen! Choosing for you.\n")
    user_option = random.randint(1, 3)
    print(f"You chose: {user_option}\n")

# Seeker warning
print("The seeker is coming!")

# Time to go hide
while countdown > 0:
    countdown -= 1
    print(countdown)
    time.sleep(1)

# Seeker picks a spot to check
get_spot = random.randint(1, 3)

print("Ready or not, here they come!")

# Allows the seeker to seek, random time added to give suspense
while seeking_time < random.randint(5,10):
    seeking_time += 1
    print("...")
    time.sleep(1)

print(f"The seeker chose: {get_spot}\n")

# Variable to see if the player won
winner = False

# Win/Lose conditions
if get_spot == user_option:
    print("You were found!\n")
else:
    print("You were NOT found!\n")
    winner = True

# Round recap
print("===ROUND RECAP===\n")

print(f"[You chose: {user_option}]\n")

print(f"[The hider chose: {get_spot}]\n")

if winner == True:
    print("[You won!]\n")
else:
    print("[You lost!]\n")
