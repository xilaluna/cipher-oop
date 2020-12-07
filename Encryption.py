from Transform import Transform
import base64
import string
import collections


class Encryption(Transform):
    """
    Encrypts users message
    """

    def base64_encrypt(self, message):
        message_ascii = message.encode('ascii')
        base64_bytes = base64.b64encode(message_ascii)
        encoded_message = base64_bytes.decode('ascii')
        return encoded_message

    def caesar_cipher_encrypt(self, message, shift_num):
        uppercase_alphabet_list = collections.deque(string.ascii_uppercase)
        lowercase_alphabet_list = collections.deque(string.ascii_lowercase)

        uppercase_alphabet_list.rotate(shift_num)
        lowercase_alphabet_list.rotate(shift_num)

        upper = ''.join(list(uppercase_alphabet_list))
        lower = ''.join(list(lowercase_alphabet_list))

        uppercase_replacement = string.maketrans(string.ascii_uppercase, upper)
        lowercase_replacement = string.maketrans(string.ascii_lowercase, lower)

        encoded_message = message.translate(
            uppercase_replacement).translate(lowercase_replacement)
        return encoded_message

    def transform(self):
        pass
