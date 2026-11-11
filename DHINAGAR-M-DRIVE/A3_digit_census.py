'''
Conditional chexks within loop to check each digits group with % operator 
'''

x=int(input("Enter integer: "))
o,e,z=0,0,0
while x>0:
    if (x%10)==0:
        z+=1
    elif (x%10)%2==0:
        e+=1
    else:
        o+=1
    x//=10
    
print(f"Odd digits   : {o}\nEven digits  : {e}\nZero digits  : {z}")

