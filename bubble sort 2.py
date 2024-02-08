my_list = []

cond = True

while cond == True:


    
    x = int(input("You need to input 5 numbers: "))
    my_list.append(x)
    if len(my_list) == 1:
        x = int(input("You need to input 4 more numbers: "))
        my_list.append(x)
    if len(my_list) == 2:
        x = int(input("You need to input 3 more numbers: "))
        my_list.append(x)
    if len(my_list) == 3:
        x = int(input("You need to input 2 more numbers: "))
        my_list.append(x)
    if len(my_list) == 4:
        x = int(input("You need to input 1 more number: "))
        my_list.append(x)





    if len(my_list) == 5:
        print("You have entered all the neccessary numbers. Thank you!")
        cond = False

    





print()
print()
print("This is the original list:\n",my_list,sep="")
print()
print()







swapped = True

while swapped == True:
    swapped = False
    for x in range(len(my_list)-1):
        if my_list[x] > my_list[x + 1]:
            swapped = True
            my_list[x] , my_list[x + 1] = my_list[x + 1] , my_list[x]







print("This is the ordered list:\n",my_list,sep="")
