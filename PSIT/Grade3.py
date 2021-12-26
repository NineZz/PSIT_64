"""Grade III"""
def upper_path(score):
    """return grade"""
    if score >= 95:
        return 4
    if score >= 90:
        return 3.5
    if score >= 85:
        return 3
    if score >= 80:
        return 2.5

def lower_path(score):
    """return grade"""
    if score >= 75:
        return 2
    if score >= 70:
        return 1.5
    if score >= 65:
        return 1.0
    if score >= 60:
        return 0.5
    if score >= 0:
        return 0

def get_grade(score):
    """return your grade"""
    if score > 100 or score < 0:
        return "ERR"
    if score >= 80:
        return upper_path(score)
    return lower_path(score)

def main():
    """function grade"""
    sum_grade = 0
    counter = int(input())
    for _ in range(counter):
        sum_grade += get_grade(float(input()))
    answer = sum_grade/counter
    return "%.2f"%(answer*100//1/100)

print(main())
