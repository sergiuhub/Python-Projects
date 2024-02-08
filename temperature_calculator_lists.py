temp = [[0.0 for h in range(24)] for d in range(31)]
##print(temp)


temp[0][22] = 31.5
temp[1][15] = 23.5
temp[3][2] = 40
temp[6][21] = -2.3
temp[3][6] = - 0.7
temp[5][5] = 14.5
temp[3][3] = 5.4
temp[7][8] = 22.6
temp[5][19] = 6.6



total = 0.0

for days in temp:
    total += days[12]

average = total / 31
print("The total average is" , average)   

print()
print()

highest = -99999
lowest = 9999999

for days in temp:
    for x in days:
        if x > highest:
            highest = x

for days in temp:
    for y in days:
        if y < lowest:
            lowest = y

            
print("The highest temperature was of" , str(highest) + ".")

print("The lowest temperature was of" , str(lowest) + ".")
    
print()
print()
hot_days = 0
cold_days = 0

for days in temp:
    for hot in days:
        if hot > 20:
            hot_days += 1

for days in temp:
    for cold in days:
        if cold < 7 and cold != 0:
            cold_days += 1


print("Hot days:" , hot_days)
print("Cold days:" , cold_days)
