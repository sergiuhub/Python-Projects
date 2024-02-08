print("Hello!")
print("\n"*3)
a = int(input("Define a: "))
b = int(input("Define b: "))
c = a == b

print("\n"*3)
if c:
    d = int(input("Define d: "))
    print()
    if d >= 10:
        print("d is bigger than 10.\nLet's multiply it by 2!")
        print()
        de = 2 * d
        print("We have \"de\" defined as " + str(de) + ".")
        print()
        if de + 25 <= 100:
            print(str(de + 25) + " " + "is lower or equal to 100!")
        elif de + 25 > 100:
            print("The number is bigger than 100!")
        elif de + 25 <= 100:
            print("The number is lower or equal to 0!")
    
        
    else:
        print("d is smaller than 10!")
else:
    print("Give two equal values!")
    a = float(input("define a, again: "))
    b = float(input("define b, again: "))
    print()
    c = a == b
    print(c)
    print()
    if c:
        print("Congrats!")
    else:
        print("Failure!")
print("\n"*6)
print("Goodbye!")






