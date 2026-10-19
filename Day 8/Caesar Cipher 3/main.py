from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    game_over = False
    while not game_over:
        def encrypt(text, shift):
            encrypted_message = ""
            for letter in text:
                if letter not in alphabet:
                    encrypted_message += letter
                else:
                    index_value = alphabet.index(letter)
                    index_value_new = (index_value + shift) % 26
                    encrypted_letter = alphabet[index_value_new]
                    encrypted_message += encrypted_letter
            print(f'Here is the encoded result: {encrypted_message}')

        def decrypt(text, shift):
            decrypted_message = ""
            for letter in text:
                if letter not in alphabet:
                    decrypted_message += letter
                else:
                    index_value = alphabet.index(letter)
                    index_value_new = (index_value - shift) % 26
                    decrypted_letter = alphabet[index_value_new]
                    decrypted_message += decrypted_letter
            print(f'Here is the decrypted result: {decrypted_message}')

        if direction == 'encode':
            encrypt(text, shift)
        elif direction == 'decode':
            decrypt(text, shift)

        choice = input("Type 'encode' to encode another message, or 'decode' to decode another message, or 'stop' to stop the program: \n").lower()
        if choice == 'stop':
            game_over = True
            print('**************** SECRET MESSAGE PROCEDURE TERMINATED ****************')
        elif choice == 'encode' or choice == 'decode':
            direction = choice
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))


caesar(text, shift, direction)



