import base64
import binascii
import hashlib
import os

from Crypto.Cipher import AES


class AESCipher:

    def __init__(self, key):
        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw: str) -> bytes:
        if not isinstance(raw, str):
            raw = str(raw)
        raw = self._pad(raw)
        iv = os.urandom(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def decrypt(self, enc) -> str:
        try:
            enc = base64.b64decode(enc)
        except binascii.Error:
            return ''
        iv = enc[:self.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[self.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.block_size - len(s) % self.block_size) * chr(self.block_size - len(s) % self.block_size)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]


aes = AESCipher(os.environ.get('AES_KEY', '0' * 32))
