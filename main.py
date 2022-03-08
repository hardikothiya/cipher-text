alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = str(input("Type 'encode' to encrypt, type 'decode' to decrypt:\n"))
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(p_text, shift_amount):
  cipyher_text = ''
  for letter in p_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    new_letter = alphabet[new_position]
    cipyher_text += new_letter
  print(cipyher_text)

def decrypt(p_text, shift_amount):
 decrypted_text = ''
 for letter in p_text:
  position = alphabet.index(letter)
  new_position = position - shift_amount
  new_letter = alphabet[new_position]
  decrypted_text += new_letter
 print(decrypted_text)

if direction == 'encode':
  encrypt(p_text = text, shift_amount = shift)
elif direction == 'decode':
  decrypt(p_text = text, shift_amount = shift)
