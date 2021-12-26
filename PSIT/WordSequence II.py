"""WordSequence II"""
def main(val1, val2):
    """WordSequence II"""
    for i in range(max(len(val1), len(val2))+1):
        print(val2[:i]+val1[i:])
main(input(), input())
