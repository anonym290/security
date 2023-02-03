arr = [30,40,2,3,68,89,245]

maximum = arr[0]

for x in range(0, len(arr)):
    if(arr[x] > maximum):
        maximum = arr[x]

print(maximum)
