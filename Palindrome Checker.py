# Written by Christian Simmons
# Palindrome Checker

#Start
print("=== Palindrome Checker ===\n")

# Get a word from the user and strip it
user_input = input("Enter the word you would you like to check: ").strip()

# Confirmation
if user_input:
     print(f"\n[You entered: {user_input}]\n")
elif not user_input:
    print("[ERROR! Nothing was entered!]\n")

# Counts how many numbers are in the word
check_word = len(user_input)

# What does the word look like forward
frontwards_string = user_input[0:check_word]

# What does the word look like backward
backwards_string = user_input[::-1]

# Debugging print to check what the output is for each
# print(frontwards_string, backwards_string)

# Checker
if frontwards_string == backwards_string:
    print(f"'{user_input}' is a palindrome.\n")
else:
     print(f"'{user_input}' is not a palindrome.\n")