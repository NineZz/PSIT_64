"""[Midterm] SecondConverter"""
def main():
    """SecondConverter"""
    num_k = int(input())
    num_s = int(input())
    num_m = int(input())
    num_h = int(input())
    minute = num_k//num_s
    hour = minute//num_m
    print("%d:%d:%d"%(hour%num_h, minute%num_m, num_k%num_s))
main()
