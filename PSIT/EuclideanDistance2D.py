"""EuclideanDistance2D"""
def main():
    """function input"""
    num_1 = float(input())
    num_2 = float(input())
    num_3 = float(input())
    num_4 = float(input())
    print(distance(num_1, num_2, num_3, num_4))

def distance(numa, numb, numc, numd):
    """function distance"""
    import math
    ans = math.sqrt(((numa-numc)**2)+((numb-numd)**2))
    return ans
main()
