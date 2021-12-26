"""Robot I"""
def main():
    """function check"""
    name = str(input())
    year = float(input())
    if 0 < year < 18:
        print("%s, you can pass."%name)
    elif year >= 18:
        print("%s, you shall not pass."%name)
main()
