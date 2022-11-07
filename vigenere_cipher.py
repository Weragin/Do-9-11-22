from vigenere import encrypt, decrypt


def encode(message: str, key:str) -> str:
    return encrypt(message, key)


def decode(message: str, key:str) -> str:
    return decrypt(message, key)
