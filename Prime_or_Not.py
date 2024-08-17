n = int(input("Enter the number: "))


def if_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
    return True


if if_prime(n):
    print(f"the given number {n} is Prime.")
else:
    print(f"the given number {n} is not Prime.")
