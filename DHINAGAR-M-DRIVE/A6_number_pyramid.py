'''
using nested loops with inner loops range relave to outer loop to print numbera and spaces to form a pyramid.
'''
x=int(input("Enter number: "))
for i in range(1, x+1):
    for j in range(i, x):
        print(" ", end="")
    for j in range(1, i+1):
        print(f"{j}  ", end="")
    print("\n")