"""[Midterm] Sequence XXX"""
def main():
    """[Midterm] Sequence XXX"""
    num_n = int(input())
    num_m = int(input())
    lines = ""
    for i in range(-(num_n//2), (num_n//2)+1):
        lines = ""
        for j in range(-(num_n//2), (num_n//2)+1):
            if j == -(num_n//2) or j == num_n//2 or\
                 i == -(num_n//2) or i == num_n//2 or abs(i) == abs(j):
                lines += "*"
            else:
                lines += " "
        print((lines+" ")*num_m)
main()
