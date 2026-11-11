'''
add if-else with A1 
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

if r==x:
    print("Result: palindrome.")
else:
    print("Result: not a palindrome.")
