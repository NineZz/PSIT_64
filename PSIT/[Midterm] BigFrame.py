"""[Midterm] BigFrame"""

def main():
    """function frame"""
    word_1 = input().strip()
    word_2 = input().strip()
    word_3 = input().strip()
    word_4 = input().strip()
    word_5 = input().strip()
    check_max = max(len(word_1), len(word_2), len(word_3), len(word_4), len(word_5))
    print("*"*(check_max+4))
    print("* "+"%s"%word_1+" "*(check_max-len(word_1))+" *")
    print("* "+"%s"%word_2+" "*(check_max-len(word_2))+" *")
    print("* "+"%s"%word_3+" "*(check_max-len(word_3))+" *")
    print("* "+"%s"%word_4+" "*(check_max-len(word_4))+" *")
    print("* "+"%s"%word_5+" "*(check_max-len(word_5))+" *")
    print("*"*(check_max+4))
main()
