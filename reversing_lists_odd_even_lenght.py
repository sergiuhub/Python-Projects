print("22 elements lists; even number")
list =[]
for i in range(22):
    list.append(i)

print(list)
print("The lenght of the list is" + " " + str(len(list)) + ".")
print()
print()

for x in range(len(list)//2):
    list[x],list[len(list)-x-1] = list[len(list)-x-1],list[x]
print("Reversing it:")
print(list)
print()
print()
print()


print("23 elements lists; odd number")
list2 = []
for z in range(23):
    list2.append(z)

print(list2)
print("The lenght of the list is" + " " + str(len(list2)) + ".")
print()
print()

for y in range(len(list2)//2):
    list2[y],list2[len(list2)-y-1] = list2[len(list2)-y-1],list2[y]
print("Reversing it:")
print(list2)
