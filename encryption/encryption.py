import sys


KEY =  {"A": "O", "B": "C", "C": "V", "D": "S", "E": "I", "F": "F", "G": "D", "H": "N", "I": "U", "J": "W", "K": "J", "L": "R", "M": "B",
        "N": "Y", "O": "M", "P": "K", "Q": "L", "R": "E", "S": "P", "T": "A", "U": "X", "V": "Z", "W": "Q", "X": "T", "Y": "G", "Z": "H"}

keyList = []
for key in KEY:
    keyList.append(key)

def main():

    if len(sys.argv) != 2:
        sys.exit("Usage: encryption.py encrypt\n       encryption.py decrypt")

    arg = sys.argv[1].lower()
    if arg != "encrypt" and arg != "e" and arg != "decrypt" and arg != "d":
        sys.exit("Usage: encryption.py encrypt\n       encryption.py decrypt")
    
    text = input("Text: ")

    if arg == "encrypt" or arg == "e":
        text = encrypt(text)
    else:
        text = decrypt(text)


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

    print(f"Encrypted text: {new_text}")

    return


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

    print(f"Decrypted text: {new_text}")

    return


main()