from transform import Transform
from encryption import Encryption
import string
import base64


class Decryption(Transform):
    """
    Decrypts user message
    """

    def __init__(self, message):
        self.message = message

    def base64_decrypt(self):
        base64_bytes = self.message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        decoded_message = message_bytes.decode('ascii')
        print(decoded_message)

    def caesar_cipher_decrypt(self):
        encrypt = Encryption(self.message)
        for i in range(len(string.ascii_uppercase)):
            print(f'{i} | {encrypt.caesar_cipher_encrypt(i)}')

    def transform(self, cipher):
        if cipher == 'base64':
            return self.base64_decrypt()
        elif cipher == 'caesar cipher':
            return self.caesar_cipher_decrypt()
