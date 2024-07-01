#To find x using modular division.

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
        
print("MODULAR DIVISION")
print("Ax ≈ B mod M")
a = int(input("Enter A: "))
b = int(input("Enter B: "))
m = int(input("Enter M: "))
Inverse = Extended_Euclid(m, a)
x = Inverse * b
if x > m:
    print("x ≈ ", x - m)
else:
    print("x ≈ ", x)