import random
import string


# Function to generate the password
def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    # Define possible characters based on user preferences
    characters = string.ascii_lowercase  # Always include lowercase letters

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    # Generate password using random choices from the available characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Main program
def main():
    print("Welcome to the Password Generator!")

    # Ask user for password length
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 1:
                print("Password length must be at least 1. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a number.")

    # Ask user if they want to include uppercase letters
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'

    # Ask user if they want to include numbers
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'

    # Ask user if they want to include special characters
    use_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'

    # Generate the password
    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)

    # Print the generated password
    print("Your generated password is:", password)


# Run the program
if __name__ == "__main__":
    main()
