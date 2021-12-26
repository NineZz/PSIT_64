"""RuleofThree"""
def main():
    """RuleofThree"""
    amount = int(input())
    save_price = float("-inf")
    save_size = float("-inf")
    save_spp = float("-inf")
    for _ in range(amount):
        price = float(input())
        size = float(input())
        size_per_price = size/price
        if size_per_price > save_spp:
            save_price = price
            save_size = size
            save_spp = size_per_price
        elif size_per_price == save_spp and price < save_price:
            save_price = price
            save_size = size
            save_spp = size_per_price
    print("%.2f %.2f"%(save_price, save_size))
main()
