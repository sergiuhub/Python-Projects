print("DIGITAL CLOCK GENERATOR")
space = "\n" * 3
print(space)

hours = int(input("Please type the hours: "))
mins = int(input("Please type the minutes: "))
sec = int(input("Please type the seconds: "))
dura_hours = int(input("Please type extra hours: "))
dura_mins = int(input("Please type extra minutes: "))
dura_sec = int(input("Please type extra seconds: "))            

# 1 hour = 3600 seconds
# 1 hour = 60 minutes
# 1 minute = 60 seconds

h = (hours * 3600 + mins * 60 + sec + dura_hours * 3600 + dura_mins * 60 + dura_sec)//3600%24

if h < 10:
    h = "0" + str(h)
print(h)

m = (mins * 60 + sec + dura_mins * 60 + dura_sec)//60%60

if m < 10:
    m = "0" + str(m)
print(m)

s = (sec + dura_sec) % 60
if s < 10:
    s = "0" + str(s)

print(space)
print("The time is " + str(h) + ":" + str(m) + ":" + str(s))
# even tho variables h,m,s are strings, we should also apply
# the str() function to them because we also have the case in which
# they are > 10 and are not strings.

