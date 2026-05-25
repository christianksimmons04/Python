# Written by River Holley
# Palindrome Checker


def main() -> None:
    """
    Prompts the user for a word and checks if it is a palindrome.

    This function reads a string from user input, strips leading and trailing
    whitespace, and compares it to its reversed self to determine if it reads
    the same backward as forward.

    Returns:
        bool: True if the input is a palindrome, False otherwise.
        None: If the user provides an empty input string.
    """
    print("=== Palindrome Checker ===\n")
    user_input = input("Enter the word you would you like to check: ").strip()
    if user_input:
        print(f"\n[You entered: {user_input}]\n")
        return user_input == "".join(reversed(user_input))
    elif not user_input:
        print("[ERROR! Nothing was entered!]\n")
    
if __name__ == "__main__":
    status = "Yes, Palindrome!" if main() else "No, not Palindrome!"
    print(status)
