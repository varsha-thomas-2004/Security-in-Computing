#To factorize a number as a product of two primes.
#Fermat Factorization

import math

def Fermat(n):
    for Y in range(0,n):
        q = n + Y**2 
        X = math.sqrt(q) #X = √(n + Y²)
        if X.is_integer(): #X is taken if it is an integer
            break
    a = int(X + Y)
    b = int(X - Y)
    print(a, "*", b, "=", n)

#Main
print("FERMAT FACTORIZATION")
n = int(input("Enter an integer: "))
Fermat(n)