print("Hello!")
print()
x = 10
y = int(input("Enter a number here or type -1 to end the program: "))

while y != -1:
  if y == x:
    print("Y is equal to X" + "; " + str(y) + " = " + str(x))
    print()
  elif y > x:
    print("Y is bigger than X" + "; " + str(y) + " > " + str(x))
    print()
  elif y < x:
    print("Y is smaller than X" + "; " + str(y) + " < " + str(x))
    print()
  y = int(input("Enter a number here or type -1 to end the program: "))
  
print()
if y == -1:
  y = int(input("Please make a final comparison since you have cancelled the program (don't input \"-1\"): "))
  if y == x:
    print("Y is equal to X" + "; " + str(y) + " = " + str(x))
  elif y > x:
    print("Y is bigger than X" + "; " + str(y) + " > " + str(x))
  elif y < x:
    print("Y is smaller than X" + "; " + str(y) + " < " + str(x))



    
print()          
print("Your last comparison number is y =" + " " + str(y) + ".")
