"""CaesarV1"""
def encrypt(text, shift):
    """encryp func"""
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.isalpha() == False:
            result += char
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)

    return result

def main():
    """main func"""
    shift = int(input())
    text = input()
    print(encrypt(text, shift))

main()
