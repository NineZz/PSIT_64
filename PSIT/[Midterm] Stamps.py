"""[Midterm] Stamps"""
def main():
    """[Midterm] Stamps"""
    visits = int(input())
    every_price = int(input())
    get_stamp = int(input())
    every_stamp = int(input())
    discount = int(input())

    have_stamp = 0
    total_bill = 0
    for _ in range(visits):
        bill = int(input())

        if have_stamp >= every_stamp:
            total_want_discount = bill//discount
            if bill % discount > 0:
                total_want_discount += 1

            can_discount = have_stamp//every_stamp

            required = min(total_want_discount, can_discount)

            if required > 0:
                bill -= (required*discount)
                bill = max(bill, 0)
                have_stamp -= required*every_stamp

        if bill >= every_price:
            more_stamp = (bill//every_price)*get_stamp
            have_stamp += more_stamp
        total_bill += bill

    print(total_bill)
    print(have_stamp)
main()
