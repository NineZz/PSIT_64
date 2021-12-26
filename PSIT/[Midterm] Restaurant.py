"""[Midterm] Restaurant"""
def main():
    """[Midterm] Restaurant"""
    num_a = float(input())
    num_b = float(input())
    num_c = (100-float(input()))/100
    num_d = float(input())
    offer_price = num_a+num_d
    if offer_price >= num_b:
        offer_price = offer_price*num_c
    if num_a >= num_b:
        num_a = num_a*num_c
    if offer_price < num_a:
        print("Yes %.3f"%(num_a-offer_price))
    elif offer_price > num_a:
        print("No %.3f"%(offer_price-num_a))
    else:
        print("Yes")
main()
