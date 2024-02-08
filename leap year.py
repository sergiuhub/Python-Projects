# if leap year_ february has 29 days
# if not leap year february has 28 days


    
    

def leap(year):
    status = True
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        status = True
        return status
    else:
        status = False
        return status
        
##status1 = leap(int(input("Choose a year: ")))
##print(status1)

count = 0
years = []
while count < 5:
    year = int(input("Choose a year: "))
    status1 = leap(year)
    if status1 == True:
        count += 1
        years.append(year)
        print("You need to choose" + " " + str(5-count) + " " + "years /year.")
        print()
    else:
        print("Not a leap year!" , end =" ")
        print("You need to choose" + " " + str(5-count) + " " + "years /year.")
        count += 1
        years.append(year)
        print()
        continue

    
years.sort()
print("The years you have chosen in chronological order:" + " " + str(years))
print()


months = []
for m in range(1,13):
    months.append(m)
print("The months:" + " " + str(months))
print()
days = []
x = 0
for d in months:
    if d == 1:
        x = 31
    if d == 2:
        x = 28
    if d == 3:
        x = 31
    if d == 4:
        x = 30
    if d == 5:
        x = 31
    if d == 6:
        x = 30
    if d == 7:
        x = 31
    if d == 8:
        x = 31
    if d == 9:
        x = 30
    if d == 10:
        x = 31
    if d == 11:
        x = 30
    if d == 12:
        x = 31
    days.append(x)

print("The days in each month:" + " " + str(days))
print()


trust = []
for z in range(len(years)):
    if leap(years[z]) == True:
        trust.append(leap(years[z]))
    if leap(years[z]) == False:
        trust.append(leap(years[z]))
print("Results:" + " " + str(trust))
print()
print()
print()
print("""       /////////////////////////////////////////////////////////////
          /////////////////////////////////////////////////////////////
          /////////////////////////////////////////////////////////////
          /////////////////////////////////////////////////////////////
          /////////////////////////////////////////////////////////////""")

print()
print()
print()
pair = []

for t in range(len(years)):
    j = int(input("Type a month from 1 - 12 (corresponding to year" + " " + str(years[t]) + "): "))
    print()
    while j < 1 or j > 12:
        j = int(input("Incorrect month number. Try again for year" + " " + str(years[t]) + "."))
        print()
        
    
    if leap(years[t]) == True:
        if j == 2:
            r = 29
            pair.append(r)
        else:
            if j == 1:
                r = 31
                pair.append(r)
            if j == 2:
                r = 28
                pair.append(r)
            if j == 3:
                r = 31
                pair.append(r)
            if j == 4:
                r = 30
                pair.append(r)
            if j == 5:
                r = 31
                pair.append(r)
            if j == 6:
                r = 30
                pair.append(r)
            if j == 7:
                r = 31
                pair.append(r)
            if j == 8:
                r = 31
                pair.append(r)
            if j == 9:
                r = 30
                pair.append(r)
            if j == 10:
                r = 31
                pair.append(r)
            if j == 11:
                r = 30
                pair.append(r)
            if j == 12:
                r = 31
                pair.append(r)
    else:
        if j == 1:
            r = 31
            pair.append(r)
        if j == 2:
            r = 28
            pair.append(r)
        if j == 3:
            r = 31
            pair.append(r)
        if j == 4:
            r = 30
            pair.append(r)
        if j == 5:
            r = 31
            pair.append(r)
        if j == 6:
            r = 30
            pair.append(r)
        if j == 7:
            r = 31
            pair.append(r)
        if j == 8:
            r = 31
            pair.append(r)
        if j == 9:
            r = 30
            pair.append(r)
        if j == 10:
            r = 31
            pair.append(r)
        if j == 11:
            r = 30
            pair.append(r)
        if j == 12:
            r = 31
            pair.append(r)
        

print()
print(str(pair))
print()
print()
print("Please provide us with a year, a month and a day.")





def dayz(yr,mn,dz):
    n = 28 
    total_days = 365
    if leap(yr) == True:
        total_days = 366
        n = 29


        



    
    if mn == 1:
        dz1 = dz
        calc = total_days - (total_days - dz1)
    if mn == 2:
        dz1 = dz
        calc = total_days - (total_days - (31 + dz1))
    if mn == 3:
         dz1 = dz
         calc = total_days - (total_days - (31 + n + dz1))
    if mn == 4:
         dz1 = dz
         calc = total_days - (total_days - (31 + n + 31 + dz1))
    if mn == 5:
          dz1 = dz
          calc = total_days - (total_days - (31 + n + 31 + 30 + dz1))
    if mn == 6:
          dz1 = dz
          calc = total_days - (total_days - (31 + n + 31 + 30 + 31 + dz1))
    if mn == 7:
          dz1 = dz
          calc = total_days - (total_days - (31 + n + 31 + 30 + 31 + 30 + dz1))
    if mn == 8:
          dz1 = dz
          calc = total_days - (total_days - (31 + n + 31 + 30 + 31 + 30 + 31 + dz1))
    if mn == 9:
          dz1 = dz
          calc = total_days - (total_days - (31 + n + 31 + 30 + 31 + 30 + 31 + 31 + dz1))
    if mn == 10:
          dz1 = dz
          calc = total_days - (total_days - (31 + n + 31 + 30 + 31 + 30 + 31 + 31 + 30 + dz))
    if mn == 11:
         dz1 = dz
         calc = total_days - (total_days - (31 + n + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + dz))
    if mn == 12:
         dz1 = dz
         calc = total_days - (total_days - (31 + n + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + dz))

    
        
    
    
    return "Year" + " " + str(yr) + "......" + "day" + " " + str(calc) + "."


print()
print()
o = int(input("Type a year: "))
p = int(input("Type a month: "))
q = int(input("Type a day: "))


while leap(o) != True and q == 29:
    q = int(input("Cannot be 29th February in a non-leap year. Try again: "))





print()
print()
print(dayz(o , p , q))















# asta de sus e terminat.
# aici am ramas.
# ma gandeam sa fac o intrebare care sa intrebe useru cate luni vrea sa aleaga sa verifice intr-un an.


