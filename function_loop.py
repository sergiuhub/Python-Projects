print("Hello!")
print()
print()
def again():
    def countodd():
        print()
        for x in range(11):
            if x % 2 == 0:
                continue
            print(x)

    def counteven():
        print()
        for z in range(11):
            if z % 2 != 0 or z == 0:
                continue
            print(z)
            
    print("You can only answer with \"Odd\" or \"Even\"!")            
    answer = input("Would you like to count odd or even numbers? ")
    print()



    while answer != "Odd" and answer != "Even":
        answer = input("You can only answer with \"Odd\" or \"Even\".Try again: ")
    
    if answer == "Odd":
        countodd()
    if answer == "Even":
        counteven()
    print()
    print("You can only answer with \"Yes\" or \"No\"!")
    answer1 = input("Would you like to do this process again? ")

    while answer1 != "Yes" and answer1 != "No":
        answer1 = input("You can only answer with \"Yes\" or \"No\". Try again: ")

    if answer1 == "Yes":
        print()
        again()
    if answer1 == "No":
        print("Ok, Goodbye!")

again()

print()
print()
print("You have completed the \"semi-loop\" by using a written function!")




