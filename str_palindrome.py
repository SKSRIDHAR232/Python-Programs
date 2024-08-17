s = input("Enter the word to check Palindrome or not: ")


def Palindrome(s):
    return s == s[::-1]


if Palindrome(s):
    print(f"The entered word {s} is Palindrome.")
else:
    print(f"Enterd word {s} is not Palindrome")
