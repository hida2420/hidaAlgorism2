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

n = ii()

def f(a, b):
    return a ** 3 + (a**2)*b + a*(b**2) + b**3
ans = n**3

#abc246 D
#単調増加な2変数関数で、最小値(最大値)を求める系は
#にぶたんさくを使う
def nibutan(ans):
    for a in range(10**6+1):
        right = 10**6
        left = -1
        while right - left > 1:
            b = (right + left)//2
            x = f(a, b)
            if x >= n:
                right = b
            else:
                left = b
        x = f(a, right)
        ans = min(ans, x)
    return ans

print(nibutan(ans))

######################################################
#以下、sanoさんバージョン
# pypyで提出

# 入力の受け取り
N=int(input())

# 関数にする
def f(a,b):
    return a**3+a**2*b+a*b**2+b**3

# 答え
ans=10**20

# b=0,1,2,...10^6
# (10^6より少し大きめにしています)
for b in range(10**6+100):

    # 左端
    l=-1
    # 右端
    r=10**6+100

    # 1<(右端-左端)の間
    while 1<r-l:
        # 中央
        c=(r+l)//2
        # 計算結果がN未満なら
        if f(c,b)<N:
            # 左端=中央と更新
            l=c
        # 計算結果がN以上なら
        else:
            # 右端=中央と更新
            r=c

    # f(r,b)がそこまでの答えより小さければ答えを更新
    ans=min(ans,f(r,b))

# 答えの出力
print(ans)
