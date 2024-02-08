larg = -9999999999
counter = 0

nr = float(input("Type your number here or press \"-1\" to end it: "))

while nr != -1:
    if nr == -1:
        continue
    counter += 1
    if nr > larg:
        larg = nr
    nr = float(input("Type your number here or press \"-1\" to end it: "))
if counter != 0:
    print("The largest number is: " + str(larg))
else:
    print("You didn't enter any number / you cancelled the program!")
