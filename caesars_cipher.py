import string

alphabet = list(string.ascii_lowercase)
end_alphabet = len(alphabet)-1

direction = input("Type 'encode' to encrypt, type 'decode' to decript:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    new_text = ""
    for letter in plain_text:
        if not letter == " ":
            letter_number = alphabet.index(letter)
            new_letter_number = letter_number+shift_amount
            if new_letter_number < end_alphabet:
                new_letter = alphabet[new_letter_number]
                new_text += new_letter
            else:
                new_letter = (alphabet[new_letter_number - len(alphabet)]) 
                new_text += new_letter
        else: 
            new_text += letter
    print(f"The encoded text is: {new_text}")


encrypt(text, shift)