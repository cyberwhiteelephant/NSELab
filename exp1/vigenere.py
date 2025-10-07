def vigenere_encrypt(text, key):
    result = ""
    key = key.lower()
    for i, char in enumerate(text):
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            key_shift = ord(key[i % len(key)]) - 97
            result += chr((ord(char) - shift + key_shift) % 26 + shift)
        else:
            result += char
    return result


def vigenere_decrypt(cipher, key):
    result = ""
    key = key.lower()
    for i, char in enumerate(cipher):
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            key_shift = ord(key[i % len(key)]) - 97
            result += chr((ord(char) - shift - key_shift) % 26 + shift)
        else:
            result += char
    return result

if __name__ == "__main__":

    text = "HELLO WORLD"
    key = "KEY"

    encrypted = vigenere_encrypt(text, key)
    print("Plaintext:", text)
    print("Key:", key)
    print("Encrypted:", encrypted)

    decrypted = vigenere_decrypt(encrypted, key)
    print("Decrypted:", decrypted)
