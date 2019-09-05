l = [x-y for x in range(1,5) for y in range(1,5) ]
print(l)
num = 0
for i in l:
    if abs(i)<2:
        num = num+1

print(num)