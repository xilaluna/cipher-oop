from usermenu import UserMenu

user_cryptography = input(
    '\nWhat would you like to do: \n[1] encrypt\n[2] decrypt\n\nYour choice: ')
user_cipher = input(
    '\nwhich cipher would you like to choose: \n[1] base64\n[2] caesar cipher\n\nYour choice: ')

user_message = input('What is your message: ')

user_shift = None

if user_cryptography == 1 and user_cipher == 2:
    user_shift = input(f'shift value integer: ')

start = UserMenu(user_cryptography, user_cipher, user_message, user_shift)
start.cryptography_choice()
