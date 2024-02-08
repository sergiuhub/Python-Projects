a = float(input("Give a: "))
b = float(input("Give b: "))
c = float(input("Give c: "))
d = float(input("Give d: "))
e = float(input("Give e: "))
print()
print()

larg = a

if a == b == c == d == e:
    print("Equality!!!")

if b > larg:
    larg = b
    
if c > larg:
    larg = c
    
if d > larg:
    larg = d
    
if e > larg:
    larg = e
    
print("The largest number is" + " " + str(larg))
