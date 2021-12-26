"""PongYa"""
def main():
    """PongYa"""
    number = int(input())
    str_num = str(number)
    last = str_num[-1]
    if number%3 == 0 or last == "3":
        print("PONG")
    else:
        print(number)
main()
