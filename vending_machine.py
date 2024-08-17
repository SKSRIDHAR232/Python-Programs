d = 10
c = int(input("no of drinks needed:"))
if c < d:
    for i in range(c):
        print("take a drink")
        b = c-i-1
        if b == 0:
            print("no drinks left")
        print("num of drinks left", b)
else:
    print("not enough")
print("Have a nice drink!")
