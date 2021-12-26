"""[Midterm] Nearer"""
def main():
    """Nearer"""
    alice = int(input())
    bob = int(input())
    ice = int(input())
    if abs(ice - bob) < abs(ice - alice):
        print("Bob %d" %(abs(ice - bob)))
    elif abs(ice - bob) > abs(ice - alice):
        print("Alice %d" %(abs(ice - alice)))
    elif abs(ice - bob) == abs(ice - alice):
        print("Sundaes %d" %(abs(ice - alice)))
main()
