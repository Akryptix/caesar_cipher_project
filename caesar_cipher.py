def caesar_cipher(text,shift,op_type):
    result = ""
    
    # Adjusts the shift for decryption

    if op_type == "decrypt":
        shift = -shift

    for character in text:

        # Handle lowercase letters
        if character.islower():
            start_ascii = ord('a')
            result += chr((ord(character) - start_ascii + shift) % 26 + start_ascii)

        # Handle uppercase letters
        elif character.isupper():
            start_ascii = ord('A')
            result += chr((ord(character) - start_ascii + shift) % 26 + start_ascii)
        else:
            result += character       
        
    return result

# --- User Input Section ---

text = input("Enter Your Text: ")
shift = int(input("Enter the shift: "))
op_type = input("Enter the mode, 'encrypt' or 'decrypt': ")

print()
print("Your final result: " + caesar_cipher(text,shift,op_type))
