#To find the multiplicative inverse in modular arithmetic.

#Extended Euclid's Algorithm
def Extended_Euclid(a, b):
    t1 = 0
    t2 = 1
    x = a
    while b != 0:
        t = t1 - (a//b)*t2
        r = a % b
        a = b
        b = r
        t1 = t2
        t2 = t
    else:
        if t1 < 0:
            return x + t1
        else:
            return t1

#Main
print("MULTIPLICATIVE INVERSE USING EXTENDED EUCLID'S ALGORITHM")
print("Constraint: a > b")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("Multiplicative inverse of ", b," mod ", a,": ", Extended_Euclid(a, b))
