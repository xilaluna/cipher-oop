import cipher
import Encryption
import Decryption


class UserMenu():
    """
    takes in user input
    """

    def __init__(self, cryptography, cipher, message):
        self.cryptography = cryptography
        self.cipher = cipher
        self.message = message

    def cryptography_choice(self):
        if self.cryptography == 'encrypt':
            Encryption(message)
        elif self.cryptography == 'decrypt':

    def user_chipher(self):
        if self.cipher == 'base64':
            return
