print("Hello! This is an example of a loop!")
z = True
while z == True:
  y = int(input("Type here 0 to end the loop: "))
  print()
  if y == 0:
    z = False
    print()
  else:
    print("Try again!")
    
print("The loop has ended!")
