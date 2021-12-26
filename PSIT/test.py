def maiin():
    """maiin"""
    num = int(input())
    for row in range(-(num-1), num):
        for col in range(-(num-1), num):
            if num-abs(row) >= abs(col)+1:
                print("%02d"%(num-abs(col)-abs(row)), end=" ")
            else:
                print("  ", end=" ")
        print()
maiin()