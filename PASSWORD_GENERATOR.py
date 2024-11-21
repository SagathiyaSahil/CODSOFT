import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special, exclude_ambiguous):
    """Generates a random password with the specified options."""
    if length < 1:
        return "Password length must be at least 1."

    # Define character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    ambiguous = 'ilLIoO01'  # Characters to exclude if specified

    # Build the character set
    characters = ""
    if use_lowercase:
        characters += lower
    if use_uppercase:
        characters += upper
    if use_numbers:
        characters += digits
    if use_special:
        characters += special
    if exclude_ambiguous:
        characters = ''.join(c for c in characters if c not in ambiguous)

    # Validate the character set
    if not characters:
        return "Error! No character types selected."

    # Generate password
    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    print("Welcome to the Advanced Password Generator!")

    try:
        # Get user input for password customization
        num_passwords = int(input("How many passwords would you like to generate? "))
        length = int(input("Enter the desired password length: "))
        
        print("\nChoose character options (y/n):")
        use_uppercase = input("Include uppercase letters? ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? ").lower() == 'y'
        use_numbers = input("Include numbers? ").lower() == 'y'
        use_special = input("Include special characters? ").lower() == 'y'
        exclude_ambiguous = input("Exclude ambiguous characters (e.g., 1, l, 0, O)? ").lower() == 'y'

        # Generate and display passwords
        print("\nGenerated Password(s):")
        for _ in range(num_passwords):
            password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special, exclude_ambiguous)
            print(password)

    except ValueError:
        print("Invalid input! Please enter valid numbers.")

if __name__ == "__main__":
    main()
