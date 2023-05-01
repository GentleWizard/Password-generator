import random
import string

# Function to generate password based on specified parameters
def Generate_password(length, uppercase=False, lowercase=False, symbols=False, numbers=False ):
    password_choices = list()
    # If lowercase letters are requested, add them to the password choices list
    if lowercase:
        password_choices.append(string.ascii_lowercase)
    # If uppercase letters are requested, add them to the password choices list
    if uppercase:
        password_choices.append(string.ascii_uppercase)
    # If numbers are requested, add them to the password choices list
    if numbers:
        password_choices.append(string.digits)
    # If symbols are requested, add them to the password choices list
    if symbols:
        password_choices.extend(['&','$','?','@','#','!'])
    
    # Initialize password as None
    password = None
    # If password_choices is not empty, generate the password
    if password_choices:
        # Join together characters randomly chosen from password_choices to form the password
        password = ''.join(random.choice(random.choice(password_choices)) for _ in range(length))
    
    # Return the generated password (or None if no password was generated)
    return password

# Function to validate user input for y/n questions
def logic(case):
    # Loop until the user enters a valid response (either 'y' or 'n')
    while case not in ['y', 'Y', 'n', 'N']:
        print('Error: Answer not valid. Please enter "y" or "n".')
        case = input('numbers? (Y/N) ')
    
    # If the user entered 'y' or 'Y', return True, otherwise return False
    if case == 'y' or case == 'Y':
        return True
    else:
        return False

# Get the desired password length from the user
length = int(input('Enter a password length: '))
# Loop until the user enters a valid password length (a positive integer)
while length < 1:
    length = int(input('Error: Password length must be a positive integer. Enter a password length: '))

# Get the user's choices for password generation
number = logic(input('numbers? (Y/N) ')) 
uppercase = logic(input('Uppercase? (Y/N) '))
lowercase = logic(input('Lowercase? (Y/N) '))
symbols = logic(input('symbols? (Y/N) '))

# Generate the password based on the user's choices
password = (Generate_password(length = int(length), uppercase=uppercase, lowercase=lowercase, numbers=number, symbols=symbols,))


# If a password was generated, print it to the console
if password:
    print(f"Generated password: {password}")
else:
    print("Failed to generate password.")
    
# Wait for the user to press enter before exiting
input('Press ENTER to exit...')