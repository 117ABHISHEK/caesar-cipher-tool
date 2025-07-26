def caesar_cipher(message, shift, mode='encode'):
    result = ''
    shift = shift % 26
    if mode == 'decode':
        shift = -shift
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Example usage
if __name__ == "__main__":
    msg = "Hello, World!"
    encoded = caesar_cipher(msg, 3)
    decoded = caesar_cipher(encoded, 3, mode='decode')
    print("Encoded:", encoded)
    print("Decoded:", decoded)
