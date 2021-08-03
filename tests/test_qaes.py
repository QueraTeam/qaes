from unittest import TestCase

from qaes.encryption import AESCipher


class QAESTest(TestCase):

    def setUp(self) -> None:
        self.AES_KEY = '0' * 32
        self.cipher = AESCipher(self.AES_KEY)

    def test_not_equal_encryption_on_randomly_mode(self):
        plain = "some plain text"
        cipher_text1 = self.cipher.encrypt(plain)
        cipher_text2 = self.cipher.encrypt(plain)
        self.assertNotEqual(cipher_text1, cipher_text2)

    def test_decryption(self):
        plain = (
            "this is a very long lorem ipsum raw string text which "
            "I wanted to place here to test the encryption method. "
            "We are being appreciated to test everything in our codebase!"
        )
        cipher_text = self.cipher.encrypt(plain)
        decrypted = self.cipher.decrypt(cipher_text)
        self.assertEqual(plain, decrypted)

    def test_padding(self):
        text = 'text'.encode('utf-8')
        padded_text = self.cipher._pad(text)
        self.assertTrue(len(padded_text), self.cipher.block_size)

    def test_unpadding(self):
        text = 'text'
        padded_text = 'text' + '\x0c' * (self.cipher.block_size - len(text))
        unpadded_text = self.cipher._unpad(padded_text)
        self.assertEqual(text, unpadded_text)

    def test_equal_encryption_on_not_randomly_mode(self):
        plain = "some plain text"
        cipher_text1 = self.cipher.encrypt(plain, randomly=False)
        cipher_text2 = self.cipher.encrypt(plain, randomly=False)
        self.assertEqual(cipher_text1, cipher_text2)
