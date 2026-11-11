'''
with nested for loops i*j give grid cell values with gaps adjusted based on digits.
'''

for i in range(1, 6):
    for j in range(1, 6):
        print(i*j, end="")
        if i*j<10:
            print("     ", end="")
        else:
            print("    ", end="")
    print("\n")