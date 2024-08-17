n = int(input("Enter the number to find the Factorial: "))


def Factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * Factorial(n-1)


print(f"Factorial of {n} is {Factorial(n)}.")
