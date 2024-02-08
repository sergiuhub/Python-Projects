

x = int(input("type a number here: "))
print()



shop = ["milk", "sugar", "fruits", "meat" + " " + "eggs", "salt", "oil"]
while 2 + x > len(shop) - 1:
    print("Error")
    x = int(input("type a number here: "))



print()
y = 2 + x
print("The element you have selected in the list is number" + " " + str(y) + " " + "by counting it in the \"Python\" way.")
print()


print("The element selected is" + " " + "\"" +shop[2+x] + "\"" + ".")
print()
print("The list has" + " " + str(len(shop)) + " " + "elements.")
print()

z = input("Would you like to replace this item? Type \"Yes\" or \"No\": ")
print()

while z != "Yes" and z!="No":
    print("You can only type \"Yes\" or \"No\"!")
    z = input("Do you like to replace this item? Type \"Yes\" or \"No\": ")
    if z == "Yes" or z == "No":
        break

if z == "Yes":
    replace = input("What would you like to replace it with?")
    shop[2+x] = replace
print()
print("This is your new list of groceries:")
print(shop)




if z == "No":
    print("Goodbye!")

