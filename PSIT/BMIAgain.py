"""BMIAgain"""
def bmi():
    """function BMI"""
    weight = int(input())
    height = float(input())
    ans = weight/(height/100)**2
    if ans < 18.5:
        print("Underweight")
    elif 18.5 <= ans < 25:
        print("Normal")
    elif 25 <= ans < 30:
        print("Overweight")
    elif ans >= 30:
        print("Obese")
bmi()
