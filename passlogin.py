import getpass

# Correct username and password
correct_username = 'bela'
correct_password = '2313'

# Function to check the credentials
def check_credentials(username, password):
    if username == correct_username and password == correct_password:
        return True
    else:
        return False

# Main program loop
for i in range(5):  # Allow 5 attempts
    username = input('Username: ')
    password = getpass.getpass('Password: ')  # Hide the password input

    if check_credentials(username, password):
        print('Welcome ')
        break
    else:
        if i < 5:  # If there are attempts left
            print('Incorrect login. Please try again.')
        else:
            print('Sorry, you are limited.')