"""CoinChangev1"""
def main(money=int(input())):
    """CoinChangev1"""
    c25 = money//25
    c10 = (money%25)//10
    c05 = ((money%25)%10)//5
    print(c25+c10+c05+(((money%25)%10)%5))
main()
