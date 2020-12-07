import cipher
import Encryption
import Decryption


class UserMenu():
    """
    takes in user input
    """

    def __init__(self, cryptography, cipher):
        self.cryptography = cryptography
        self.cipher = cipher

    def user_cryptography(self):
        pass

    def user_chipher(self, cipher):
        if self.cipher == 'base64':
            return
