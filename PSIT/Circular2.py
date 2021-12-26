"""Circular II"""
def distance(numa, numb, numc, numd):
    """function distance"""
    import math
    ans = math.sqrt(((numa-numc)**2)+((numb-numd)**2))
    return ans
def main():
    """function circle"""
    num_xm = float(input())
    num_ym = float(input())
    num_rm = float(input())
    num_xf = float(input())
    num_yf = float(input())
    num_rf = float(input())
    if distance(num_xm, num_ym, num_xf, num_yf) < num_rm + num_rf:
        print("Yes")
    else:
        print("No")
main()
