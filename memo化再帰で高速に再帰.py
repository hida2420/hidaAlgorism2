N = int(input())
memo = {}

def f(n):
    if n == 0:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = f(n//2) + f(n//3)
        return memo[n]
    
print(f(N))