"""PrasomSib"""
def main(val=input(), count=0):
    """PrasomSib"""
    for j in range(len(val)):
        num = int(val[j])
        for i in range(j+1, len(val)):
            num += int(val[i])
            if num == 10:
                count += 1
            if num >= 10:
                break
    print(count)
main()
