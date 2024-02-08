pyramid = []
number = 0

for i in range(1, 11):
    row = ""
    for j in range(1, i + 1):
        number += 1
        row += str(number) + " "
    pyramid.append(row)

for row in pyramid:
    print(row)
