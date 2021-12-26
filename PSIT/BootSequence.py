"""BootSequence"""
def main():
    """function boot"""
    num_list = []
    number = int(input())
    for i in range(1, number+1):
        num_list.append(i)
    print(*num_list, sep="_")
main()
