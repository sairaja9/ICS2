#Pythagorean Sequence in Python
# Copyright © 2019, Sai K Raja, All Rights Reserved

def Pythagorean_Theorem(a, b):
    if a > 0 and b > 0:
        return a**2 + b**2

    elif a < 0 or b < 0:
        print("Cannot use negative values in Pythagorean Theorem")

for i in range (1):
    print(Pythagorean_Theorem(3, 6))
    