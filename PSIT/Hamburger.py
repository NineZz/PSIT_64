"""Hamburger"""
def main():
    """function hamburger"""
    bread_1 = int(input())
    bread_2 = int(input())
    meat = (bread_1*2) + (bread_2*2)
    print("|"*bread_1 + "*"*meat + "|"*bread_2)
main()
