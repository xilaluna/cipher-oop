from Transform import Transform
import Encryption
import string
import base64


class Decryption(Transform):
    """
    Decrypts user message
    """

    def base64_decrypt(self, message):
        base64_bytes = message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        decoded_message = message_bytes.decode('ascii')
        print(decoded_message)

    def caesar_cipher_decrypt(self, message):
        for i in range(len(string.ascii_uppercase)):
            print(f'{i} | {Encryption.caesar_cipher_encrypt(message, i)}')

    def transform(self, cipher, message):
        if cipher == 'base64':
            return self.base64_decrypt(message)
        elif cipher == 'caesar cipher':
            return self.caesar_cipher_decrypt(message)
