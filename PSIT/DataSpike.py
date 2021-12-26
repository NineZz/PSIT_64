"""DataSpike"""
def check(xxxx, yyyy):
    """function check"""
    return xxxx > yyyy and xxxx or yyyy

def main():
    """function max"""
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())
    num_4 = int(input())
    num_5 = int(input())
    num_6 = int(input())
    num_7 = int(input())
    num_8 = int(input())
    print("%d"%check(check(check(check(check(check(check(num_1, num_2), \
        num_3), num_4), num_5), num_6), num_7), num_8))
main()
