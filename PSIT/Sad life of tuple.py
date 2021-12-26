"""Sad life of tuple"""
def main(data, val):
    """Sad life of tuple"""
    data = data.split()
    for _ in range(data.count(val)):
        for _ in range(data.count(val)):
            print(data.index(val), end=' ')
        print()
main(input(), input())
