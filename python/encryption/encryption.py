import sys


KEY =  {"A": "O", "B": "C", "C": "V", "D": "S", "E": "I", "F": "F", "G": "D", "H": "N", "I": "U", "J": "W", "K": "J", "L": "R", "M": "B",
        "N": "Y", "O": "M", "P": "K", "Q": "L", "R": "E", "S": "P", "T": "A", "U": "X", "V": "Z", "W": "Q", "X": "T", "Y": "G", "Z": "H"}

keyList = []
for key in KEY:
    keyList.append(key)

def main():

    # Error message for incorrect command-line arguments
    errorMsg = "Usage: encryption.py encrypt [filename.txt]\n       encryption.py decrypt [filename.txt]"

    # Check amount of command-line arguments
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        sys.exit(errorMsg)
    
    # Check first argument
    arg = sys.argv[1].lower()
    if arg != "encrypt" and arg != "e" and arg != "decrypt" and arg != "d":
        sys.exit(errorMsg)
    
    # If a text file was specified in command-line arguments, read and write to that file
    if len(sys.argv) == 3:
        with open(sys.argv[2], "r") as file:
            text = file.read()
        if arg == "encrypt" or arg == "e":
            text = encrypt(text)
        else:
            text = decrypt(text)
        with open(sys.argv[2], "w") as file:
                file.write(text)
    # If a text file was not specified, prompt user for text and output encrypted/decrypted text to terminal
    else:
        text = input("Text: ")
        if arg == "encrypt" or arg == "e":
            text = encrypt(text)
            print(f"Encrypted text: {text}")

        else:
            text = decrypt(text)
            print(f"Decrypted text: {text}")


# Encrypt text
def encrypt(text):

    new_text = ""

    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                new_text += KEY[letter]
            else:
                new_text += KEY[letter.upper()].lower()
        else:
            new_text += letter

    return new_text


# Decrypt text
def decrypt(text):

    new_text = ""

    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                new_text += (list(KEY.keys())[list(KEY.values()).index(letter)])
            else:
                new_text += (list(KEY.keys())[list(KEY.values()).index(letter.upper())]).lower()
        else:
            new_text += letter

    return new_text


main()