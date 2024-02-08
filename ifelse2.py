print("Hello!")
print("\n"*3)
a = float(input("define a: "))
b = float(input("define b: "))
c = a == b
#print(a)
#print(b)
print("\n"*3)
if c:
    print("The numbers are equal! Let's also round them!")


    x = a
    y = b
    a = round(a)
    b = round(b)
    print(x,"rounded is " + str(a) + "..... " + "is a.")
    print(y,"rounded is " + str(b) + "..... " + "is b.")
else:
    print("No, the 2 numbers aren't equal.\nLet's round them!")
    print()
#print(a)
#print(b)

    print("Remember a = " + str(a))
    print("Remember b = " + str(b))
    print()
    print("a rounded is equal to" + " " + str(round(a)))
    print("b rounded is equal to" + " " + str(round(b)))

print("\n"*2)
print("Rate our example please!")
mark = float(input("Give us a mark from 0 to 10 please: "))
mark_1 = int(mark)
print("You marked us with" + " " + str(mark))
print("\n"*2)

if mark < 0:
    print("You cannot give negative marks!")
elif mark > 10:
    print("You cannot give marks bigger than 10!")

else:
    print("Thank you for you feedback!\nGoodbye!")









