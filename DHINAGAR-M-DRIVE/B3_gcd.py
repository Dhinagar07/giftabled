'''
looping till min(x,y) and assign gcd to i if both x and y are divisible by i
'''
x=int(input("Enter number1: "))
y=int(input("Enter number2: "))
for i in range(1, min(x,y)+1):
    if x%i==0 and y%i==0:
        gcd=i
print(f"GCD of {x} , {y} : {gcd}")