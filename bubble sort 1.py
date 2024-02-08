print("Hello!")
print()
print()
total = int(input("How many elements you want in your list? "))
print()
mylist = []

cond = True

while cond == True:
    
    x = float(input("Type here a number: "))
    mylist.append(x)
    if len(mylist) == total:
        cond = False
print()
print()
print("This is your original list:\n" + str(mylist))
print()
ask = input("Would you like to sort it? Answer \"Yes\" or \"No\": ")
print()



while ask != "Yes" and ask != "No":
    ask = input("Please answer the previous question only with \"Yes\" or \"No\"! ")
    print()






if ask == "No":
    print("Ok, your list stays as it is!")
    print(mylist)
    print()
    print("Goodbye!")

if ask == "Yes":



    swapped = True

    while swapped == True:
        swapped = False
        for y in range(total - 1):
            if mylist[y] > mylist[y+1]:
                mylist[y] , mylist[y+1] = mylist[y+1] , mylist[y]
                swapped = True
    print("Your ordered list is:\n" + str(mylist),sep ="")





            
            
