"""[Midterm] Milk V.1"""
def main():
    """[Midterm] Milk V.1"""
    price = int(input())
    cap = int(input())
    get = int(input())
    money = int(input())

    get_milk = money//price
    if cap > 0:
        cap_cumulative = get_milk
        while cap_cumulative >= cap:
            get_more_milk = (cap_cumulative//cap)*get
            cap_cumulative %= cap
            cap_cumulative += get_more_milk
            get_milk += get_more_milk
    print(get_milk)
main()
