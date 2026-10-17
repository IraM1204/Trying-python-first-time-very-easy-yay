alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encrypted_message = " "
    for letter in text:
        index_value = alphabet.index(letter)
        index_value_new = (index_value + shift) % 26
        encrypted_letter = alphabet[index_value_new]
        encrypted_message += encrypted_letter
    print(f'Here is the encoded result: {encrypted_message}')

encrypt(text, shift)