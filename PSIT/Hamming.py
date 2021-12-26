"""Hamming"""
def main(word1, word2):
    """main"""
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    print(count)
main(list(input()), list(input()))
