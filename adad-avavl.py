x = int(input('Enter Number => '))

a = 0

for i in range(1 , x+1):
    if x % i == 0:
        a += 1
if a == 2:
    print("Addad Shoma Aval Ast")
else:
    print("Adad Shoma Aval Nist")
