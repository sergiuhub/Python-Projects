##Let's assume that you've chosen the following numbers in the lottery: 3, 7, 11, 42, 34, 49.
##
##The numbers that have been drawn are: 5, 11, 9, 42, 3, 49.
##
##The question is: how many numbers have you hit?


lottery = [5 , 11 , 9 , 42 , 3 ,49]

chosen =[]
count = 0



    



while len(chosen) < len(lottery):
    

    x = int(input("Choose a number: "))
    if x >= 0 and x <= 100:
        chosen.append(x)
        
    while x < 0 or x > 100:
        x = int(input("You cannot choose negative numbers or numbers bigger than 100. Try again: "))
        if x > 0 and x <= 100:
            chosen.append(x)
            break
        
print()
print()
print("Your chosen numbers:")
print(chosen)
print()
print("Lottery winner numbers:")
print(lottery)
print()
print()
hits = 0
for number in chosen:
    if number in lottery:
        hits += 1

print(hits)



