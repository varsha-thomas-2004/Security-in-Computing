#To find the Greatest Common Divisor of 2 numbers.

#Euclid's Algorithm
def Euclid (a,b):
    if b == 0:
        return a
    else:
        return Euclid (b, a % b)
            
#Main   
print("EUCLID'S ALGORITHM FOR GREATEST COMMON DIVISOR")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("GCD: ", Euclid(a,b))