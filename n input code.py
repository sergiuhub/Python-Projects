print("Hello!","Try this one out!",sep=".....",end=" ")
print("It's amazing!")
print()
exe = int(input("How many lines do you want to leave as spacing:"))
print(exe)
print("Spacing chosen displayed below as empty lines:")
print("\n"*(exe-1)) # (exe-1) because if i put simply "exe" it will give me 6 lines instead of 5.

print("You entered",exe,"as number of lines.")



