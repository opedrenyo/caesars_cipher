import string

from art import logo

print(logo)

alphabet = list(string.ascii_lowercase)
end_alphabet = len(alphabet)-1

def cipher(plain_text, shift_amount):
    new_text = ""
    for letter in plain_text:
        if letter.isalpha():
            letter_number = alphabet.index(letter)
            if direction == "encode":
                new_letter_number = letter_number+shift_amount
                if new_letter_number < end_alphabet:
                    new_letter = alphabet[new_letter_number]
                    new_text += new_letter
                else:
                    new_letter = (alphabet[new_letter_number - len(alphabet)]) 
                    new_text += new_letter
            elif direction == "decode":
                new_letter_number = letter_number-shift_amount
                new_letter = alphabet[new_letter_number]
                new_text += new_letter
            else: 
                print(f"This {direction} direction is not right.")
                break
        else: 
            new_text += letter
    print(f"The {direction}d text is: {new_text}")

should_continue = True
while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decript:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    cipher(text,shift)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye")





