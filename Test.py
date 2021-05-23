import math
for i in range(2000, 3200):
    if i % 7 == 0 and i % 5 != 0:
        if i > 3193:
            print(i)
            break;
        print(i, end=",")



first = input()
last = input()

first = first[::-1]
last = last[::-1]

print(first + ' ' + last)

diameter = 12
print(4/3*math.pi*diameter)


