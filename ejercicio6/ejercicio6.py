import math


a = int(input("se agrega el valor de a: "))
b = int(input("se agrega el valor de b: "))
c = int(input("se agrega el valor de c: "))

# processing

d=b**2-4*a*c

if d == 0:
    x1=(b/2*a)
    x2=x1
    print(x1, x2)


if d>0:
        x1=(-b+math.sqrt(d))/(2*a)
        x2=(-b-math.sqrt(d))/(2*a)
        print(x1, x2)
        
else:
        print("las raices son imaginarias")