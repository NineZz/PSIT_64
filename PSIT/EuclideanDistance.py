"""EuclideanDistance"""
def main(num=int(input()), ans=0):
    """EuclideanDistance"""
    point1 = input().split()
    for _ in range(num-1):
        point2 = input().split()
        ans += ((int(point1[0])-int(point2[0]))**2+(int(point1[1])-int(point2[1]))**2)**0.5
        point1 = point2
    print('%.2f' %ans)
main()
