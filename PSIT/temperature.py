"""temperature"""
def fah(num, unit):
    """fah"""
    if unit == "C":
        return (num-32)*(5/9)
    elif unit == "K":
        return (num-32)*(5/9)+273.15
    elif unit == "R":
        return ((num-32)*(5/9)+273.15)*9/5
def kel(num, unit):
    """kel"""
    if unit == "C":
        return num-273.15
    if unit == "F":
        return ((num-273.15)*(9/5))+32
    if unit == "R":
        return num*(9/5)
def ran(num, unit):
    """ran"""
    if unit == "C":
        return num*5/9-273.15
    elif unit == "F":
        return (num*5/9-273.15)*9/5+32
    elif unit == "K":
        return num*5/9
def cel(num, unit):
    """cel"""
    if unit == "F":
        return (num*(9/5))+32
    if unit == "K":
        return num+273.15
    if unit == "R":
        return (num+273.15)*(9/5)
def main():
    """temperature"""
    num_1 = float(input())
    unit_1 = input()
    unit_2 = input()
    if unit_1 == unit_2:
        print("%.2f"%num_1)
    elif unit_1 == "F":
        print("%.2f" %fah(num_1, unit_2))
    elif unit_1 == "C":
        print("%.2f" %cel(num_1, unit_2))
    elif unit_1 == "K":
        print("%.2f" %kel(num_1, unit_2))
    elif unit_1 == "R":
        print("%.2f" %ran(num_1, unit_2))
main()
