''' 
divide number x by 2 to x//2 and check if remainder is 0 then it is not a prime number
'''
x=int(input("Enter integer: "))
d=0
if x<2:
    print(f"{x} not a prime number.")
    exit()
for i in range(2,x//2):
    if x%i==0:
        d=i
        break
if d>0:
    print(f"{x} is divisible by {d}.\n{x} is not a prime number.")
else:
    print(f" {x} is a prime number.")