def fib(n, item1=0, item2=1):
    if n > 1:
        return fib(n-1, item2, item1+item2)
    else:
        return (item1, item2)[n]


print(fib(0))
