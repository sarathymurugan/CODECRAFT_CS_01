def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result


def decrypt(cipher_text, shift):
    return encrypt(cipher_text, -shift)


# ---- MAIN PROGRAM ----
print("=== Caesar Cipher Tool ===")
message = input("Enter your message: ")
shift = int(input("Enter shift value (1-25): "))

encrypted = encrypt(message, shift)
decrypted = decrypt(encrypted, shift)

print("\nEncrypted Text :", encrypted)
print("Decrypted Text :", decrypted)
