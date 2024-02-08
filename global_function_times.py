def aug(x, i = 1):
    global var , tar , par
    var = 100 + (x * i)
    tar = 200 + (x * i)
    par = 300 + (x * i)

add = int(input("Choose 1 or 2 or 3 as identation: "))

while add != 1 and add != 2 and add != 3:
    add = int(input("Choose only 1 or 2 or 3 as identation. Try again: "))
    print()

print("Choose maximum of 15 repetitions.")
times = int(input("How many times would you like to make the calculation? "))
print()

while times < 1 or times > 15:
    if times < 1:
        times = int(input("Not less than 1 repetition. Try again: "))
        print()
    if times > 15:
        times = int(input("Not more than 15 repetitions. Try again: "))
        print()


print("You have chosen to add" + " " + str(add) + " " + "for" + " " + str(times) + " times.")
print()
aug(add , times)
print(var)
print(tar)
print(par)
    

