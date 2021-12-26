"""[Midterm] ValidVar"""
import keyword
def main():
    """check"""
    max_input = int(input())
    for i in range(max_input):
        word = input()
        word = word.strip()
        num_w = word.isdigit()
        if i == max_input:
            break
        if keyword.iskeyword(word) == True or " " in word or \
            word.isidentifier() == False or num_w == True:
            print("Invalid")
        else:
            print("Valid")
main()
