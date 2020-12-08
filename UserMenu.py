from encryption import Encryption
from decryption import Decryption


class UserMenu():
    """
    takes in user input
    """

    def __init__(self, cryptography, cipher, message, shift_num='1'):
        self.cryptography = cryptography
        self.cipher = cipher
        self.message = message
        self.shift_num = shift_num

    def cryptography_choice(self):
        if self.cryptography == '1':
            encryption = Encryption(self.message)
            return encryption.transform(self.cipher, self.shift_num)
        elif self.cryptography == '2':
            decryption = Decryption(self.message)
            return decryption.transform(self.cipher)
