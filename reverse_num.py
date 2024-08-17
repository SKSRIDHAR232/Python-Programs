a = int(input("Enter the number to be Reversed: "))


def ReverseNum(a):
    Reversed_num = 0
    while a > 0:
        remainder = a % 10
        Reversed_num = Reversed_num * 10 + remainder
        a = a // 10
    return Reversed_num


print(f"The reversed number using math method is {ReverseNum(a)}.")


def Reversed(a):
    reversed = int(str(a)[::-1])
    return reversed


print(f"The reversed number using array method is {Reversed(a)}.")
