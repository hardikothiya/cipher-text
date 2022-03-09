alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(p_text, shift_amount, sl_direction):
    text = ''
    for letter in p_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if sl_direction == 'encode':
                new_position = position + shift_amount

            elif sl_direction == 'decode':
                new_position = position - shift_amount

            new_letter = alphabet[new_position]
            text += new_letter


        else:
            text += letter

    print(text)


should_end = False
while not should_end:
    direction = str(input("Type 'encode' to encrypt, type 'decode' to decrypt:\n"))
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 25
    run_again = 'true'

    caesar(p_text=text, shift_amount=shift, sl_direction=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
