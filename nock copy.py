def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a, b = map(int, input().split())

gcd_value = gcd(a, b)

count = abs(a // gcd_value - b // gcd_value)

print(count)
