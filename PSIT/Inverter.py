"""Inverter"""
def main():
    """Inverter"""
    num = input()
    num_n = ""
    for i in num:
        if i == "0":
            num_n += '1'
        elif i == "1":
            num_n += "0"
    print(num_n.lstrip('0'))
main()
