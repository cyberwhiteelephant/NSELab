def caesar_encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(cipher, key):
    return caesar_encrypt(cipher, -key)

if __name__ == "__main__":
    text = "HELLO WORLD"
    key = 3

    encrypted = caesar_encrypt(text, key)
    print("Plaintext:", text)
    print("Encrypted:", encrypted)

    decrypted = caesar_decrypt(encrypted, key)
    print("Decrypted:", decrypted)
