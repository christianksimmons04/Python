# Written by Christian Simmons
# Create A Dog

#Class

class Dog:
    #Attributes
    name = ""
    breed = ""
    color = ""
    gender = ""
    def get_details(my_dog):
        name_input = input("Choose a name: ")
        breed_input = input("Choose a breed: ")
        color_input = input("Choose a color: ")
        gender_input = input("Choose a gender: ")
        print(f"Dog name: {name_input} | Dog breed: {breed_input} | Dog color: {color_input} | Dog gender: {gender_input}")

user_dog = Dog()

user_dog.get_details()