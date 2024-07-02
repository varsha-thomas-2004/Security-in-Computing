#To check whether a given number is prime or not.
#Miller - Rabin's Primality Test

import random

def Odd(x):
    k = 0
    while x % 2 == 0:
        k += 1
        x = x//2 
    else:
        m = x #Odd number obtained after repeatedly dividing x by 2
    return k, m #n - 1 = 2^k * m

def Miller_Rabin(n):
    x = n - 1
    k, m = Odd(x)
    a = random.randint(2, n - 2) #chooses a, such that 1 < a < n - 1 
    b = pow(a, m, n) #b = a^m(mod n)
    while k != 0 and b != 1:
        if b == x: #b = -1
            print(n, "is probably prime.")
            break
        else:
            b = pow(b**2, m, n) #b = b^2(mod n)
        k -= 1
    else: #b = 1
        print(n, "is composite.")


#Main
print("MILLER RABIN PRIMALITY TEST")
n = int(input("Enter an integer: "))
if n == 1:
    print("1 is neither prime nor composite.")
elif n == 2 or n == 3:
    print(n, "is probably prime.")
else:
    Miller_Rabin(n)