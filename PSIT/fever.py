"""Fever"""
def main(cel=float(input())):
    """Fever"""
    if cel < 36:
        print('hypothermia')
    elif 36 <= cel < 38:
        print('No Fever')
    elif 38 <= cel < 39:
        print('Mild Fever')
    elif 39 <= cel < 40:
        print('High Fever')
    else:
        print('Very High Fever')
main()
