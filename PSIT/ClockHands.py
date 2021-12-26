"""ClockHands"""
X1, X2 = int(input()), int(input())
print(X2 <= ((((X1 * 5)) + (X2 / 12)) % 60) < X2 + 1)
