"""Circular I"""
def distance(numa, numb, numc, numd):
    """function distance"""
    import math
    ans = math.sqrt(((numa-numc)**2)+((numb-numd)**2))
    return ans
def main():
    """function circle"""
    num_x = float(input())
    num_y = float(input())
    num_r = float(input())
    num_xm = float(input())
    num_ym = float(input())
    if distance(num_x, num_y, num_xm, num_ym) <= num_r:
        print("Yes")
    else:
        print("No")
main()
