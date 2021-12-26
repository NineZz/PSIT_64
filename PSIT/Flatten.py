"""Flatten"""

import json


def check_flatten(num):
    """check flatten func"""
    list_num = []
    for i in num:
        if isinstance(i, int):
            list_num.append(int(i))
        else:
            list_num.extend(check_flatten(i))
    return list_num


def main():
    """main func"""
    num = json.loads(str(input()))
    num = check_flatten(num)
    print(sorted(num, reverse=True))


main()
