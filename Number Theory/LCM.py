#To find the Least Common Multiple.

#Euclid's Algorithm for GCD
def Euclid (a,b):
    if b == 0:
        return a
    else:
        return Euclid (b, a % b)
    
#Main   
print("LEAST COMMON MULTIPLE")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
GCD = Euclid(a, b)
if a < 0:
    LCM = -(a * b) / GCD
else:
    LCM = (a * b) / GCD
print("LCM: ", LCM)
