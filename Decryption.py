from Transform import Transform
import Encryption
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
        return decoded_message

    def caesar_cipher_decrypt(self):
        for i in range(len(string.ascii_uppercase)):
            print(f'{i} | {Encryption.caesar_cipher_encrypt(self.message, i)}')

    def transform(self):
        pass
