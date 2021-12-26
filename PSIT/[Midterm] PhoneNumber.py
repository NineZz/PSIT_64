"""[Midterm] PhoneNumber"""
def main():
    """number"""
    number = input()
    word = input()
    if len(number) == 9 and word == "Domestic":
        print(number[0], number[1:5], number[5:9])
    elif len(number) == 9 and word == "International":
        print("+66", number[1:5], number[5:9])
    if len(number) == 10 and word == "Domestic":
        print(number[0:2], number[2:6], number[6:10])
    elif len(number) == 10 and word == "International":
        print("+66"+number[1], number[2:6], number[6:10])
main()
