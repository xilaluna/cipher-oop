from usermenu import UserMenu

user_cryptography = input(
    'What would you like to do decrypt/encrypt: ')
user_cipher = input(
    'which cipher would you like to choose base64 or ceaser cipher: ')
user_message = input('What is your message: ')

start = UserMenu(user_cryptography, user_cipher, user_message)
start.cryptography_choice()
