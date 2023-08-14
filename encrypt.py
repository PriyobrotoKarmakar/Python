alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)
def ceaser(text,shift,direction):
    end_text = ""
    if direction == "decode":
        shift *= -1
    elif direction == "encode":
        shift *= 1
    else:
        print("invalid input")
    

    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift
            if new_position > 25:
                new_position2 = (shift-(25-position))-1
                new_letter = alphabet[new_position2]
                end_text +=new_letter

            elif new_position < 0 :
                new_position2 = 26-((-1*shift)-position)
                new_letter = alphabet[new_position2]
                end_text +=new_letter
            else:
                new_letter = alphabet[new_position]
                end_text += new_letter
        else:
            end_text += letter
    print(f"Your {direction} text is {end_text}")       

result_selection = True
while  result_selection:       
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(text,shift,direction)
    result = input("If you want to go again type 'yes', Otherwise 'no':\n")
    if result == 'no':
        result_selection = False
print("Goodbye")