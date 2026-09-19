def caesar_cipher(text, shift, mode='encode'):
    result = ""
    if mode == 'decode':
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result

if __name__ == "__main__":
    message = input("Enter your message: ")
    shift_amount = int(input("Enter shift number: "))
    
    encrypted = caesar_cipher(message, shift_amount, mode='encode')
    print(f"Encrypted message: {encrypted}")

    decrypted = caesar_cipher(encrypted, shift_amount, mode='decode')
    print(f"Decrypted message: {decrypted}")
