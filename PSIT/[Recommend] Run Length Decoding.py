"""[Recommend] Run Length Decoding"""
def main():
    """[Recommend] Run Length Decoding"""
    word = input()
    answer = ""
    collector = ""
    for char in word:
        if char.isnumeric():
            collector += char
        else:
            answer += "%s"%(char*int(collector))
            collector = ""
    print(answer)
main()
