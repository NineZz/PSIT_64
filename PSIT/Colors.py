"""Colors"""
def main():
    """function main"""
    color_1 = input()
    color_2 = input()
    color_lst = ['Red', 'Yellow', 'Blue']
    if color_1 not in color_lst or color_2 not in color_lst:
        print('Error')
    elif color_1 == color_2:
        print(color_1)
    elif (color_1 == 'Red' and color_2 == 'Yellow') or (color_2 == 'Red' and color_1 == 'Yellow'):
        print('Orange')
    elif (color_1 == 'Red' and color_2 == 'Blue') or (color_2 == 'Red' and color_1 == 'Blue'):
        print('Violet')
    elif (color_1 == 'Blue' and color_2 == 'Yellow') or (color_2 == 'Blue' and color_1 == 'Yellow'):
        print('Green')
main()
