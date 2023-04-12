def factorial():
    n = int(input())
    fact = 1
    i = 1
    while i <= n:
        fact = fact*i
        i = i+1
    return fact




n = int(input())


def factorial_recurs(n):
    if n == 1:
        return n
    else:
        return n*factorial_recurs(n-1)


y = factorial_recurs(n)
print(y)
