# Written by Christian Simmons
# Win At Betting or Something

# Imports
import random
import time

# Global variables
user_name = input("What is your name: ") # Player name
is_active = True # Is the game playing
winning_horse = 0

print("=== Betting Game ===\n You have seven days to win over 100 dollars!\n Bad things will happen if you don't...") # Premise

print("IMPORTANT:\n 1. Each day you must bet on a new horse! It may have the same name as a previous horse, but this one is different!\n 2. You have to pick randomly! You know almost nothing about the horses except some stats!\n 3. Just like in real betting it is pure luck!") # Will add more

class Horse:
    def __init__(self):
        self._generate_stats()  # Generate stats automatically on creation

    def _generate_stats(self, name=None): # Main stat generator
        self.name = name or self._generate_name()
        self.speed = random.randint(60, 95)
        self.stamina = random.randint(60, 95)
        self.temperament = random.randint(40, 90)
        self.experience = random.randint(1, 50)

    def _generate_name(self): # Name generator
        name_list = ["Shirley", "Knox", "Tide", "Carl", "Gary", "Diana", 
                    "Shipgold", "Slow", "Junebug", "Rainbow", "Lawnmower", 
                    "Jackson", "Orange", "Lamp", "Larry", "Pewdiepie"]
        self.name = random.choice(name_list)
        return self.name

    def __str__(self):
        return f"{self.name} (Spd:{self.speed} Sta:{self.stamina})"
    
    def __repr__(self):
        return self.__str__()
    
class Game: # Game class
    def __init__(self):
        self.current_day = 0
        self.deadline = 7
        self.player_money = 10
        self.target = 100  

    def start(self): # Main game loop lives here
        print("=== Todays contestants ===\n")

        # Generate fresh horses every day
        horse_one = Horse()
        horse_two = Horse()
        horse_three = Horse()

        contestants = [horse_one, horse_two, horse_three]

        print(f"1. {contestants[0]}, 2. {contestants[1]}, 3. {contestants[2]}")

        user_input = input("Choose your horse (INTEGER): \n")
        user_input_int = int(user_input)
        user_bet = input("How much do you want to bet: \n")
        user_bet_int = int(user_bet)

        if user_input_int >= 4:
            print("[ERROR! Your ignorance has costed you! Also, you got ran over by a horse and sadly passed away.]")
            self.player_money = 0
            self.deadline = 7

        if user_bet_int >= self.player_money:
            print("[ERROR! You have been caught trying to use counterfeit money. As a result, you're now sleeping with the fishes...]")
            self.player_money = 0
            self.deadline = 7

        horse_one_result = horse_one.speed + horse_one.stamina + horse_one.experience - horse_one.temperament
        horse_two_result = horse_two.speed + horse_two.stamina + horse_two.experience - horse_two.temperament
        horse_three_result = horse_three.speed + horse_three.stamina + horse_three.experience - horse_three.temperament

        if horse_one_result > horse_two_result or horse_three_result:
            print(f"{horse_one} has won!")
            winning_horse = 1
            if user_input_int == winning_horse:
                print("You won!")
                self.player_money = self.player_money + user_bet_int * 2
                print(f"You have: ${self.player_money}")
            else:
                print("You lost!")
                self.player_money = self.player_money - user_bet_int
                print(f"You have: ${self.player_money}")
        elif horse_two_result > horse_one_result or horse_three_result:
            print(f"{horse_two} has won!")
            winning_horse = 2
            if user_input_int == winning_horse:
                print("You won!")
                self.player_money = self.player_money + user_bet_int * 2
                print(f"You have: ${self.player_money}")
            else:
                print("You lost!")
                self.player_money = self.player_money - user_bet_int
                print(f"You have: ${self.player_money}")
        elif horse_three_result > horse_one_result or horse_two_result:
            print(f"{horse_three} has won!")
            winning_horse = 3
            if user_input_int == winning_horse:
                print("You won!")
                self.player_money = self.player_money + user_bet_int * 2
                print(f"You have: ${self.player_money}")
            else:
                print("You lost!")
                self.player_money = self.player_money - user_bet_int
                print(f"You have: ${self.player_money}")

        self.current_day = self.current_day + 1
        print(f"Day: {self.current_day}")

game = Game()

while is_active == True:
    if is_active == True and game.player_money > 0:
        game.start()
    elif game.player_money > 100:
        print(f"You win, {user_name}!")
        break
    elif game.player_money <= 0:
        print("GAME OVER!")
        break
