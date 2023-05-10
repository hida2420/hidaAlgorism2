#入力一行を配列に
def il(): return [int(x) for x in input().split()]
def i(): return input()
def ii(): return int(input())
def im(): return map(int, input().split())
def ims(): return map(str, input.split())
#N行分の2値入力(整数)
def imfn(n): return [im() for i in range(n)]
#N行分の2値入力(文字列)
def imsfn(n): return [ims() for i in range(n)]
#N行分の配列入力
def ilfn(n): return [il() for i in range(n)]
def ifn(n): return [i() for j in range(n)]
def iifn(n): return [ii() for i in range(n)]

#引数：累積和を求める配列、N
#例えば、1~3番目の要素の和を求める場合、C[3]-C[1]で求める
def CUSUM(A, n):
    #累積和の計算
    C = [0]*(n+1)
    for i in range(n):
        C[i+1] = C[i]+A[i]
    return C

#bの値を10^6とする
B = 10**6
#10^6までの中の素数をTrueにする
is_prime = [True]*B

#0, 1は素数ではない
is_prime[0] = False
is_prime[1] = False

#エラスとてネスの篩
for i in range(B):
    if is_prime[i]:
        for j in range(i*i, B, i):
            is_prime[j] = False

#10^6までの全ての素数
primes = [i for i in range(B) if is_prime[i]]

n = ii()
ans = 0

#aだけで考えたときに
#aの5乗がnをこえたら絶対ダメだからbreakして...
#という感じで全探索をする
#10^6までならこれで間に合う
#
#1回目のfor文では、a^2*b*c^2をa^5で考える
#2回目のfor文では、a^2*b*c^2をa^2*b^3で考える
#3回目のfor文では、a^2*b*c^2で考える
cnt_primes = len(primes)
for i in range(cnt_primes):
    a = primes[i]
    if a**5 > n:
        break

    for j in range(i+1, cnt_primes):
        b = primes[j]
        if (a**2)*(b**3) > n:
            break

        for k in range(j+1, cnt_primes):
            c = primes[k]
            if (a**2)*b*(c**2):
                break
            ans += 1
print(ans)