"""scale"""

def main():
    """not scalar just scale"""
    inp_m = int(input())
    inp_n = int(input())
    lst = []
    ans = ""
    for _ in range(inp_m * inp_n):
        inp = float(input())
        lst.append(inp)
    most, less = max(lst), min(lst)
    for i in range(len(lst)):
        lst[i] = (lst[i]-less) / (most-less)
    for i in range(inp_m):
        for j in range(1, inp_n+1):
            ans += "%.2f " %lst[((i*inp_n)+j)-1]
        ans += "\n"
    print(ans)
main()
