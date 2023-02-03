x = input('Enter String ... : ')

for i in range (0 , len(x)):
    count = 1
    for s in range(i+1 , len(x)):
        if(x[i] == x[s] and x[i] !=""):
            count += 1
    if count > 1:
        print(x[i])
