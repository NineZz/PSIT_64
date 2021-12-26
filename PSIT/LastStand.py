"""LastStand"""
def main():
    """LastStand"""
    import json
    num_list = json.loads(input())
    for i in num_list:
        print(i%10)
main()
