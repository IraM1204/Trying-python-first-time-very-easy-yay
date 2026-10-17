alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")
#
# encrypt(original_text=text, shift_amount=shift)
def caesar(text, shift):

    def encrypt(text, shift):
        encrypted_message = " "
        for letter in text:
            index_value = alphabet.index(letter)
            index_value_new = (index_value + shift) % 26
            encrypted_letter = alphabet[index_value_new]
            encrypted_message += encrypted_letter
        print(f'Here is the encoded result: {encrypted_message}')

    def decrypt(text, shift):
        decrypted_message = " "
        for letter in text:
            index_value = alphabet.index(letter)
            index_value_new = (index_value - shift)
            decrypted_letter = alphabet[index_value_new]
            decrypted_message += decrypted_letter
        print(f'Here is the encoded result: {decrypted_message}')

    if direction == 'encode':
        encrypt(text, shift)
    elif direction == 'decode':
        decrypt(text, shift)

caesar(text, shift)
# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.



