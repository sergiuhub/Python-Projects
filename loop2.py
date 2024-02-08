print("Hello!")
print()
x = True
while x == True:
  print("Type 0 to cancel the program.")
  y = int(input("Type here a number: "))
  
  if y == 0:
    x = False

  else:
    print("You chose the number:" + " " + str(y))
    print()
  
if y == 0:
  print()
  print("You entered \"0\"!")
  print("The program has ended! Goodbye!")          
          
  
          
