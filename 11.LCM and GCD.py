import math

def lcm_gcd(a, b):
    gcd = math.gcd(a, b)
    lcm = abs(a * b) // gcd
    return lcm, gcd

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

lcm, gcd = lcm_gcd(a, b)
print("LCM:", lcm)
print("GCD:", gcd)
