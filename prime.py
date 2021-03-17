n=int(input("Enter Number: "))

for i in range(2,n):
    if n%i==0:
        print("not Prime")
        break
else:
    print("Prime")
