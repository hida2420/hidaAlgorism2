def gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcd(b, a % b)
        return d, y, x - (a //b) * y
    
a, b = map(int, input().split())

d, x, y = gcd(a, b)
print(abs(x) + abs(y))