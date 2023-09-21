from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function to encrypt or decrypt.
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char not in alphabet:
      end_text += char
      continue
    position = alphabet.index(char)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
  print(f"Here's the {cipher_direction}d result: {end_text}")

# Printing logo from other file
print(logo)

repeat = "yes"

while repeat == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  # Looping back the shift value in case its very large
  if shift > 26:
    shift = shift % 26

  # Calling the main caesar cipher function
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
