n = int(input("Enter the total number of Series: "))


def fibonacciSeries(n):
    series = [0, 1]
    for i in range(2, n):
        nxt_val = series[-1] + series[-2]
        series.append(nxt_val)
    return series


print(f"The Fibonacci series for the number {n} is: {fibonacciSeries(n)}")
