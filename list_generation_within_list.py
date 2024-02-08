list = []

while len(list) != 7:
    x = int(input("Type a number here: "))
    list.append(x)

print()
print(list)

list2=[]


##VARIANTA CARE SI EA MERGE:
##for x in list:
##    if x >= 0:
##        list2.append(x)
##
##print()
##print(list2)

list3 =[y for y in list if y >= 0]
print(list3)
