"""BMI"""
def main():
    """function input"""
    name_1 = input()
    weight_1 = float(input())
    height_1 = float(input())
    name_2 = input()
    weight_2 = float(input())
    height_2 = float(input())
    name_3 = input()
    weight_3 = float(input())
    height_3 = float(input())
    name_4 = input()
    weight_4 = float(input())
    height_4 = float(input())
    name_5 = input()
    weight_5 = float(input())
    height_5 = float(input())
    print("%s's  BMI = %.2f"%(name_1, bmi(weight_1, height_1)))
    print("%s's  BMI = %.2f"%(name_2, bmi(weight_2, height_2)))
    print("%s's  BMI = %.2f"%(name_3, bmi(weight_3, height_3)))
    print("%s's  BMI = %.2f"%(name_4, bmi(weight_4, height_4)))
    print("%s's  BMI = %.2f"%(name_5, bmi(weight_5, height_5)))

def bmi(num_1, num_2):
    """function BMI"""
    ans = num_1/((num_2/100))**2
    return ans
main()
