

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
          'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shit_position = alphabet.index(letter) + shift_amount
            shit_position %= len(alphabet)
            output_text += alphabet[shit_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


shouldContinue = True

while shouldContinue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number: \n"))
    ceaser(original_text=text,shift_amount=shift,encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no' \n").lower()
    if restart == "no":
       shouldContinue = True
       print("Bye!")
