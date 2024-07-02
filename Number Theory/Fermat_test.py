#To check whether a given number is prime or not.
#Fermat's Primality Test

import random

def Fermat(p):
    a = random.randint(1, p - 1) #chooses a, such that 1 <= a < p
    x = a**p - a
    if x % p == 0: #is a^p - a is a multiple of p, then p is prime
        print(p, "is prime.")
    else:
        print(p, "is composite.")

#Main
print("FERMAT'S PRIMALITY TEST")
p = int(input("Enter an integer: "))
if p == 1:
    print("1 is neither prime nor composite.")
else:
    Fermat(p)
