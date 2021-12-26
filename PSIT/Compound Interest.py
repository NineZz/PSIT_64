"""Compound Interest"""
def main():
    """ahhhhhhh"""
    money = int(input())
    rate = float(input())
    year = int(input())
    for _ in range(year):
        money += (rate/100)*money
    print("%.2f"%money)
main()
