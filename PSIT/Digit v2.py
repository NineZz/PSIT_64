"""Digit v2"""
def main(word):
    """main"""
    if "thousand" in word:
        print(4)
    elif "hundred" in word:
        print(3)
    elif "ty" in word or "teen" in word or "ten" in word or "eleven" in word or "twelve" in word:
        print(2)
    else:
        print(1)

main(input())
