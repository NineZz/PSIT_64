"""ATM"""
def atm():
    """function atm"""
    money = int(input())
    while True:
        action = input()
        if action == 'END':
            break
        elif action[0] == 'D':
            money += int(action[2:])
        elif action[0] == 'W':
            if money <= int(action[2:]):
                money = 0
            else:
                money -= int(action[2:])
    print(money)
atm()
