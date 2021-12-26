"""Triangle I"""
def main():
    """Triangle I"""
    wood_1 = float(input())
    wood_2 = float(input())
    wood_3 = float(input())

    triangle_1 = abs(wood_1**2 + wood_2**2 - wood_3**2) <= 0.01
    triangle_2 = abs(wood_1**2 + wood_3**2 - wood_2**2) <= 0.01
    triangle_3 = abs(wood_2**2 + wood_3**2 - wood_1**2) <= 0.01

    if triangle_1 or triangle_2 or triangle_3:
        return "Yes"
    return "No"

print(main())
