a = int(input("Enter the number of times to be checked: "))
for i in range(1, a+1):
    n = int(input("Enter the number: "))
    if n < 0:
        print("Enter the valid number")
    elif n % 2 == 0:
        print(f"the given number {n} is EVEN.")
    else:
        print(f"the given number {n} is ODD.")
