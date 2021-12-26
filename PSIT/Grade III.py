"""Grade III"""

def main():
    """Grade III"""
    max_input = int(input())
    i = 1
    num_list = []
    while i <= max_input:
        score = float(input())
        num_list.append(score)
        i += 1

def check(score):
    """function check"""
    if 100 >= score >= 95:
        print("A")
    elif 95 > score >= 90:
        print("B+")
    elif 90 > score >= 85:
        print("B")
    elif 85 > score >= 80:
        print("C+")
    elif 80 > score >= 75:
        print("C")
    elif 75 > score >= 70:
        print("D+")
    elif 70 > score >= 65:
        print("D")
    elif 65 > score >= 60:
        print("F+")
    elif 60 > score >= 0:
        print("F")

