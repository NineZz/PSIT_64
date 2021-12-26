"""[Midterm] Pringles"""
def main():
    """[Midterm] Pringles"""
    upper = input()
    actual = input()
    lower = input()
    finger_length = int(input())

    print(actual[:finger_length].count(")"))
    if ")" in actual[finger_length:]:
        print("There are still some left.")
    else:
        print("None.")
    print(upper)
    print(" "*finger_length+actual[finger_length:])
    print(lower)
main()
