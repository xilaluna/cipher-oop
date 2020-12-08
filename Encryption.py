from transform import Transform
import base64
import string
import collections


class Encryption(Transform):
    """
    Encrypts users message
    """

    def __init__(self, message):
        self.message = message

    def base64_encrypt(self):
        message_ascii = self.message.encode('ascii')
        base64_bytes = base64.b64encode(message_ascii)
        encoded_message = base64_bytes.decode('ascii')
        print(encoded_message)

    def caesar_cipher_encrypt(self, shift_num):
        shift_num = int(shift_num)
        uppercase_alphabet_list = collections.deque(string.ascii_uppercase)
        lowercase_alphabet_list = collections.deque(string.ascii_lowercase)

        uppercase_alphabet_list.rotate(shift_num)
        lowercase_alphabet_list.rotate(shift_num)

        upper = ''.join(list(uppercase_alphabet_list))
        lower = ''.join(list(lowercase_alphabet_list))

        uppercase_replacement = str.maketrans(string.ascii_uppercase, upper)
        lowercase_replacement = str.maketrans(string.ascii_lowercase, lower)

        encoded_message = self.message.translate(
            uppercase_replacement).translate(lowercase_replacement)
        print(encoded_message)

    def transform(self, cipher, shift_num):
        if cipher == '1':
            return self.base64_encrypt()
        elif cipher == '2':
            return self.caesar_cipher_encrypt(shift_num)
