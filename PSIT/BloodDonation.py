"""BloodDonation"""
def main():
    """BloodDonation"""
    age, weight, was = int(input()), int(input()), int(input())
    if age == 17 or 60 <= age <= 70:
        book = input()
    if (age == 17 or 60 <= age <= 70) and book == 'False':
        print('No')
    elif (was == 0 and age > 55) or age < 17 or age > 70 or weight < 45:
        print('No')
    elif (age == 17 or 60 <= age <= 70) and book == 'True' and weight >= 45:
        print('Yes')
    elif 17 < age < 60 and weight >= 45:
        print('Yes')
main()
