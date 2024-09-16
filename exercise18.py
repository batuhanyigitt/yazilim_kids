

def ceaser_encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char 
    return encrypted_text

def ceaser_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - ascii_offset - shift) %26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char 
    return decrypted_text

plaintext = "merhaba"
shift = 3 
encrypted_text = ceaser_encrypt(plaintext, shift)
print("Encryted text: ", encrypted_text)

decrypted_text = ceaser_decrypt(encrypted_text, shift)
print("Decryted text: ", decrypted_text)