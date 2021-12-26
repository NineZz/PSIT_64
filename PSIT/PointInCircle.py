"""PointInCircle"""
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
    num_xn = float(input())
    num_yn = float(input())
    if distance(num_x, num_y, num_xn, num_yn) <= num_r:
        print("True")
    else:
        print("False")
main()
