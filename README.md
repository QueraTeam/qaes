# qaes
This package is an AES cryptography utility for making symmetric cipher text with CBC mode.

qaes is an abbreviation for QueraAES.

# Getting started

## Required Env Variable
Set `AES_KEY` in your env var to a string with length of 32 chars.

## Usage Example

### How to encrypt data
```python
>>> from qaes import aes
>>> plain_text = 'some random text to be encrypted'
>>> cipher_text = aes.encrypt(plain_text)
>>> print(cipher_text)
i7atAzh52yonxaVIRrz4C5g6kCQxHTVpeA/VwNHkbtjRWcblseMeCVKBSiAQLTScqO4S29+YUCaRzCbERUFQoA==
```

### How to decrypt data
```python
>>> from qaes import aes
>>> cipher_text = 'TO7vmcWssWIbmTXSM24ha0f3RpIaqgLZqlsVHwtx+CY='
>>> decrypted_text = aes.decrypt(cipher_text)
>>> print(decrypted_text)
it's a secret
```