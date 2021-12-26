"""Run Length Encoding"""
def main():
    """function main"""
    word = input()
    counter = 0
    save_char = ""
    answer = ""
    for char in word:
        if char != save_char:
            if save_char != "":
                answer += "%d%s"%(counter, save_char)
            save_char = char
            counter = 1
        else:
            counter += 1
    answer += "%d%s"%(counter, save_char)
    print(answer)
main()
