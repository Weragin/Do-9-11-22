from typing import List


def char_to_int(text) -> List[int]:
	text = text.upper()
	res = []
	for i in text:
		assert 64 < ord(i) <91, "Function only accepts alfa characters."
		res.append(ord(i) - 64)
	return res

def encrypt(text: str, key: str) -> str:
	key = char_to_int(key)
	result = ""
	
	for i in range(len(text)):
		Ord = ord(text[i])
		if 64 < Ord < 91:
			result += chr(((Ord - 65 + key[i % len(key)]) % 26) + 65)
		if 96 < Ord < 123:
			result += chr(((Ord - 97+ key[i % len(key)]) % 26) + 97)
		else: result += i
	return result


def decrypt(text: str, key: str) -> str:
	key = char_to_int(key)
	result = ""
	
	for i in range(len(text)):
		Ord = ord(text[i])
		if 64 < Ord < 91:
			result += chr(((Ord - 65 - key[i % len(key)])
										% 26) + 65)
		if 96 < Ord < 123:
			result += chr(((Ord - 97 - key[i % len(key)])
										% 26) + 97)
		else: result += i
	return result


text = input("Message: ")
key = input("Key: ")
print(f"Encrypted message is {encrypt(text, key)}.")
print(f"The message was {decrypt(text, key)}.")
