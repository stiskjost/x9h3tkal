def add(x, y):
    return x + y

def factorial(n):
    for i in range(n,1,-1):
        n *= i-1
    return n

def sin(x, N):
    s = 0
    for n in range(N+1):
        s += ((-1)**n * x**(2*n+1))/factorial(2*n+1)
    return s

def divide(x,y):
    return x/y

"""
https://en.wikipedia.org/wiki/Floor_and_ceiling_functions
"""

def ceil(x):
    return int(x // 1) + 1

"""
https://en.wikipedia.org/wiki/Digital_root
"""

def digitalRoot(n):
    k = len(list(str(n)))
    s = 0
    for i in range(k):
        di = (n % 10**(i+1) - n % 10**(i)) / 10**i
        s += int(di)
    if s >= 10:
        s = digitalRoot(s)
    return s
