import base64
import hashlib
import os
import secrets

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, modes, algorithms

backend = default_backend()


class AESCipher:

    def __init__(self, key):
        self.block_size = algorithms.AES.block_size // 8
        self.key = hashlib.sha256(key.encode()).digest()
        self.cipher = lambda iv: Cipher(algorithms.AES(self.key), modes.CBC(iv), backend)

    def encrypt(self, plain: str) -> str:
        plain = plain.encode('utf-8')
        padded_raw = self._pad(plain)
        iv = self.generate_iv()
        encryptor = self.cipher(iv).encryptor()
        cipher_text = encryptor.update(padded_raw) + encryptor.finalize()
        return base64.b64encode(iv + cipher_text).decode('utf-8')

    def decrypt(self, cipher_text: str) -> str:
        cipher_text = base64.b64decode(cipher_text)
        iv, cipher_text = cipher_text[:self.block_size], cipher_text[self.block_size:]
        decryptor = self.cipher(iv).decryptor()
        decrypted = decryptor.update(cipher_text) + decryptor.finalize()
        return self._unpad(decrypted).decode('utf-8')

    def generate_iv(self):
        return secrets.token_bytes(self.block_size)

    def _pad(self, data: bytes) -> bytes:
        index = self.block_size - len(data) % self.block_size
        data += index * chr(index).encode('utf-8')
        return data

    @staticmethod
    def _unpad(data: bytes) -> bytes:
        return data[:-ord(data[len(data) - 1:])]


aes = AESCipher(os.environ.get('AES_KEY', '0' * 32))
