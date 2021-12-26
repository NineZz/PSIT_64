"""LetterFrequency"""
def main(i, lst):
    """LetterFrequency"""
    for j in range(97, 123):
        lst.append([i.count(chr(j)), chr(j)])
    lst.sort()
    print(lst[25][1])
main(input().lower(), [])
