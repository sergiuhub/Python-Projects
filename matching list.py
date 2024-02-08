def count(x):
    while True:
        if x == "Yes":
            return True
            
        elif x == "No":
            return False
        else:
            print("Error!")
            break
            return None
print("Answer only with \"Yes\" or \"No\".")        
ask = input("Would you like to proceed? ")
print()

while ask != "Yes" and ask != "No":
    ask = input("You can only answer with \"Yes\" or \"No\". Try again: ")
    print()




if ask == "Yes":
    
    list1 = ["Yes" , "No" , "Yes" , "No" , "Yes" , "Yes" , "Yes" , "No" , "Yes" , "No"]
    list2 = [True , False , False , True , True , False , False , False , True , True]

    for y in range(len(list1)):
        number1 = list1[y]
        number2 = list2[y]
        print(number1 + " " + str(number2))
        
        check = count(number1)


        if check == list2[y]:
            print("Matches.")
            print()
        else:
            print("Doesn't match.")
            print()
            
if ask == "No":
    print("Goodbye!")




    
    


