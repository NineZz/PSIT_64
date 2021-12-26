"""Blackjack"""
def get_point(char):
    """function check"""
    if char in "JQK":
        return 10
    return int(char)

def main():
    """function main"""
    max_input = int(input())
    point = 0
    ace = 0
    for _ in range(max_input):
        hand = input()
        if hand == "A":
            ace += 1
        else:
            point += get_point(hand)

    if ace == 3:
        point = 13
    elif ace == 2:
        if point+12 > 21:
            point += 2
        else:
            point += 12
    elif ace == 1:
        if point+11 > 21:
            point += 1
        else:
            point += 11
    print(point)
main()
