"""safe"""
def main(text1, text2):
    """safe"""
    count = 0
    for i in range(len(text1)):
        fun, fun2 = abs(abs(ord(text1[i]) - ord(text2[i])) - 26), abs(ord(text1[i]) - ord(text2[i]))
        count += min(fun, fun2)
    print(count)
main(input(), input())
