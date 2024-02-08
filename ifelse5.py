print("Hello!")
space = "\n" * 3
print(space)
vreme = input("Please type \"good\" or \"bad\": ")


print()
if vreme == "good":
    print("You have chosen" + " " + vreme + " " + "weather.")
    print()
    fun1 = input("Please choose between \"picnic\" and \"running\": ")
    print()
    if fun1 == "picnic":
        print("You have chosen to go to the " + fun1 + ".")
        print("The weather is " + vreme + "." + " We will go to the " + fun1 + ".")
    elif fun1 == "running":
        print("You have chosen to go " + fun1 + ".")
        print("The weather is " + vreme + "." + " We will go " + fun1 + ".")
    else:
        print("You can either choose between \"picnic\" or \"running\"!")
    

    
elif vreme == "bad":
    print("You have chosen" + " " + vreme + " " + "weather.")
    print()
    fun2 = input("Please type \"cinema\" or \"home\": ")
    print()
    if fun2 == "cinema":
        print("You have chosen the " + fun2 + ".")
        print("The weather is " + vreme + "." + " We will go to the " + fun2 + ".")
    elif fun2 == "home":
        print("You have chosen to stay " + fun2 + ".")
        print("The weather is " + vreme + "." + " We will stay " +fun2 + ".")
    else:
        print("You can either choose between \"cinema\" or \"home\"!")

else:
    print("You didn't type \"good\" or \"bad\"!")
print(space)
print("Goodbye!")
