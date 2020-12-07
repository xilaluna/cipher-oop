import cipher
import Encryption
import Decryption


class UserMenu():
    """
    takes in user input
    """

    def __init__(self, cryptography, cipher, message, shift_num):
        self.cryptography = cryptography
        self.cipher = cipher
        self.message = message
        self.shift_num = shift_num

    def cryptography_choice(self):
        if self.cryptography == 'encrypt':
            Encryption.transform(self.cipher, self.message, self.shift_num)
        elif self.cryptography == 'decrypt':
            Decryption.transform(self.cipher, self.message)
