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