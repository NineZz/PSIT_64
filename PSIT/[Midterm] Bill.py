"""[Midterm] Bill"""
def main():
    """function bill"""
    price = int(input())
    charge_10 = price*(10/100)
    if 50 <= charge_10 <= 1000:
        price_10 = price+charge_10
    elif charge_10 < 50:
        price_10 = price+50
    elif 1000 < charge_10:
        price_10 = price+1000
    price_7 = price_10*(107/100)
    print("%.2f"%price_7)
main()
