"""[Recommend] Books"""
import math
def main():
    """[Recommend] Books"""
    book_amount = int(input())
    pages = int(input())
    read_x = int(input())
    read_y = int(input())

    days = 0
    for i in range(book_amount):
        this_book_page = pages
        pre_cal_read_per_day = (math.ceil((read_x+days)/(read_y+days)*pages))
        if pre_cal_read_per_day == pages:
            days += book_amount-i
            break
        while this_book_page > 0:
            read_per_day = (math.ceil((read_x+days)/(read_y+days)*pages))
            this_book_page -= read_per_day
            days += 1
    print(days)
main()
