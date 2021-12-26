"""Cha Cha Cha"""
import math
def main():
    """Cha Cha Cha"""
    money = 0
    days = int(input())
    while days > 0:
        hours = float(input())
        hours = math.ceil(hours)
        hours *= 8720
        money += hours
        days -= 1
    print(money)
main()
