"""PickThemAgain"""
def main():
    """PickThemAgain"""
    lines = input().split()
    num_list = []
    for i in lines:
        if int(i)%3 == 0 or int(i)%5 == 0:
            num_list.append(i)
    if len(num_list) == 0:
        print("Nope")
    else:
        for i in reversed(num_list):
            print(i)
main()
