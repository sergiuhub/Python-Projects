print("Clock generator")
hours = int(input("Hours pls: "))
mins = int(input("Minutes pls: "))
sec = int(input("Seconds pls: "))
dura_mins = int(input("Additional minutes: "))
dura_sec = int(input("Additional seconds: "))
print("\n"*3)

#1 hour = 60 minutes
#1 hour = 3600 seconds
#1 minute = 60 seconds

a = (hours * 3600 + mins * 60 + sec + dura_mins * 60 + dura_sec)//3600%24
b = (mins * 60 + sec + dura_mins * 60 + dura_sec)//60%60
c = (sec + dura_sec)%60


print(str(a),end=":")
print(str(b),end=":")
print(str(c))

