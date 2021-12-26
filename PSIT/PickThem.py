"""PickThem"""
import json
def main():
    """PickThem"""
    num_list = json.loads(input())
    even_list = []
    for i in num_list:
        if i%2 == 0:
            even_list.append(i)
    if len(even_list) == 0:
        print("Nope")
    else:
        for i in even_list:
            print(i)
main()
