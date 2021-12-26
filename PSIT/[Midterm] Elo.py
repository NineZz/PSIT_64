"""[Midterm] Elo"""
def main():
    """Elo"""
    num_a = int(input())
    num_b = int(input())
    word = input()
    elo_a = 1/(1+10**((num_b-num_a)/400))
    elo_b = 1/(1+10**((num_a-num_b)/400))
    if word == "A":
        print("%.2f"%elo_a)
    elif word == "B":
        print("%.2f"%elo_b)
main()
