"""Backward"""
def main():
    """Backward"""
    word_list = []
    while True:
        word = input()
        if word == "NULL":
            break
        else:
            word_list.append(word)
    for char in reversed(word_list):
        print(char)
main()
