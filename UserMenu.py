import cipher
import Encryption
import Decryption


class UserMenu(Encryption, Decryption):
    """
    takes in user input
    """

    def __init__(self, cipher):
        self.cipher = cipher

    def user_chipher(self, cipher):
        if cipher == 'base64':
            return
