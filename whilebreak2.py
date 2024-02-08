print("Hello!")
print()
print()
x = input("Type your name here: ")
y = int(input("Type your age here: "))

while True:
     if x != "" or y >= 18:
         break
     if x == "":
         print("You entered a blank!")
         x = input("Enter your name: ")
     if y < 18:
         print("You are younger than 18 years old!")
         y = int(input("Enter your age: "))

while x == "":
    print("You can t enter a blank!")
    x = input("Type your name here again: ")

while y < 18:
    print("You are under 18 years old!")
    y = int(input("Enter your age again: "))

print()
print()
print("Your name is" + " " + x + " and you are " + str(y) + " years old.")
