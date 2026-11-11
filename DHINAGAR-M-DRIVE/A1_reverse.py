'''
To reverse an integer I loop over the digits and build a new integer by extract remoinder (x%10) and multiply 10 to the current reversed integer 
'''

x=int(input("Enter integer: "))
r=0
while x>0:
    r*=10
    r=(r+(x%10))
    #print("Current reversed integer:", r)
    x//=10
    
    #print("Current integer:", x)
print("Reversed integer:", r)
