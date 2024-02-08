list = [[8 for x in range(5)] for y in range(4)]
print(list)
print()
print()
z = int(input("Choose a week from 1 - 4: "))



while z < 1 or z > 4:
    print("Error!")
    z = int(input("Try again: "))

if z == 1:
    w = 0
if z == 2:
    w = 1
if z == 3:
    w = 2
if z == 4:
    w = 3

print()
print("You have chosen week number" + " " + str(z) + ".")
print()
o = int(input("Choose a day between 1 - 5: "))
print()
while o < 1 or o > 5:
    print("Error!")
    o = int(input("Try again2: "))

if o == 1:
    q = 0
    print("You have chosen day number" + " " + str(o) + ", meaning Monday.")
if o == 2:
    q = 1
    print("You have chosen day number" + " " + str(o) + ", meaning Tuesday.")
if o == 3:
    q = 2
    print("You have chosen day number" + " " + str(o) + ", meaning Wednesday.")
if o == 4:
    q = 3
    print("You have chosen day number" + " " + str(o) + ", meaning Thursday.")
if o == 5:
    q = 4
    print("You have chosen day number" + " " + str(o) + ", meaning Friday.")
print()
print()
print()
print("You have chosen day" + " " + str(o) + " in week" + " " + str(z) + ".")
print()
k = int(input("So, you are saying you worked less in this particular day. How many hours did you work? "))

while k < 0 or k > 8:
    if k < 0:
        k = int(input("Cannot be negative. Try again: "))
    if k > 8:
        k = int(input("Cannot be bigger than 8. Try again: "))


print("The hours for the specified day will be changed from 8 to" + " " + str(k) + ".")
print()
list[w][q] = k
print(list)

days = 0
for lala in list[0]:
    if lala != 8:
        days +=1
        
for lala in list[1]:
    if lala != 8:
        days +=1
        
for lala in list[2]:
    if lala != 8:
        days +=1
        
for lala in list[3]:
    if lala != 8:
        days +=1
print()
print(list)
print(days)
