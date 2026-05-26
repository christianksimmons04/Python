# Written by Christian Simmons
# Hide and Seek

# Import modules
import time
import random

# Setting integer variables
countdown = 11
seeking_time = 0

# Hiding spots
set_one = ["Couch", "Chair", "TV"]
set_two = ["Table", "Recliner", "Curtain"]
set_three = ["Shower", "Closet", "Chase"]

# Set random spot
random_option_one = random.choice(set_one)
random_option_two = random.choice(set_two)
random_option_three = random.choice(set_three)

# Starting the game
print("===Enter the Number===\n")

print(f"[1] {random_option_one} | [2] {random_option_two} | [3] {random_option_three}\n")

user_option = input("Pick a hiding spot!\n")

# Options
if user_option == 1:
    print("[You chose the couch!]\n")
elif user_option == 2:
    print("[You chose the curtain!]\n")
elif user_option == 3:
    print("[You chose the shower!]\n")
else:
    print("Inavlid ineger chosen! Choosing for you.\n")
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
