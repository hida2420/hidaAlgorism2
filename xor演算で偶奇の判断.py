#abc295d

S = input()

table = [0 for i in range(2**10)]

table[0] = 1

bit = 0

for i in range(len(S)):
    s = int(S[i])

    bit ^= 2**s
    table[bit] += 1
    #print("{}番目の文字　s:{}, sの2乗:{}, bit:{}".format(i, s, s**2, bin(bit)))

ans = 0

#nC2
def combination(n):
    return n * (n - 1)//2

for t in table:
    ans += combination(t)

print(ans)