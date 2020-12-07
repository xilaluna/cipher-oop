from Transform import Transform
import base64


class Encryption(Transform):
    """
    Encrypts users message
    """

    def base64_encrypt(self, message):
        message_ascii = message.encode('ascii')
        base64_bytes = base64.b64encode(message_ascii)
        encoded_message = base64_bytes.decode('ascii')
        return encoded_message

    def cesear_cipher_encrypt(self):
        pass

    def transform(self):
        pass
