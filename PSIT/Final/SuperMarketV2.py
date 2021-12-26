"""SuperMarketV2"""
import math
def market():
    """function market"""
    num_item = int(input())
    min_cost = float(input())
    num_b = float(input())
    num_c = float(input())
    cost_lst = []
    while num_item > 0:
        cost = float(input())
        cost_lst.append(cost)
        num_item -= 1
    sum_cost = sum(cost_lst)
    max_cost = max(cost_lst)
    if sum_cost >= min_cost:
        max_cost = (num_c/100)*max_cost
        sum_cost -= max_cost
        if sum_cost >= min_cost:
            sum_cost = ((100-num_b)/100)*sum_cost
            print(math.floor(sum_cost))
        else:
            print(math.floor(sum_cost))
    elif sum_cost < min_cost:
        max_cost = (num_c/100)*max_cost
        sum_cost -= max_cost
        print(math.floor(sum_cost))
market()
