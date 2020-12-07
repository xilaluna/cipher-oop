from Transform import Transform
import base64


class Decryption(Transform):
    """
    Decrypts user message
    """

    def base64_decrypt(self, message):
        base64_bytes = message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        decoded_message = message_bytes.decode('ascii')
        return decoded_message

    def ceaser_cipher_decrypt(self):
        pass

    def transform(self):
        pass
