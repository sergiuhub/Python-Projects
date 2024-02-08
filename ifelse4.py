print("Hello!")
print("\n"*3)
a = int(input("Define a: "))
b = int(input("Define b: "))
print()
print()
c = a == b
if c:
    print("I like that this is true!")
else:
    print("Bad luck!")
    y = int(input("Type 1 or 2: "))
    print()
    if y == 1:
        print("You have chosen 1!")
    elif y == 2:
        print("You have chosen 2!")
    elif y >= 2:
        print("You have chosen the number: " + str(y))
        if y != 1 and y != 2:
            print("The number you have entered is incorrect!")
    elif y <= 1:
        print("You have chosen the number: " + str(y))
        if y != 1 and y !=2:
            print("The number you have entered is incorrect!")
print("\n"*4)
print("Goodbye!")
        
