"""[Midterm] BTSMRT"""
def main():
    """BTSMRT"""
    day = input()
    age = float(input())
    heigth = float(input())
    if day == "Children Day" and age < 14 and heigth <= 140:
        print("FREE")
    elif day == "Senior Day" and age >= 60:
        print("FREE")
    elif age < 14 and heigth < 90:
        print("FREE")
    else:
        print("PAY")
main()
