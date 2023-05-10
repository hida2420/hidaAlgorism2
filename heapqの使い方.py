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

n, k = im()
p = il()

#abc234 D(類題：abc297 E)
#heapqは小さい方からK番目のものを取り出すのに
#よく使われる
#普通のリストだと、要素の取り出し、appendにO(N)
#かかるところを、O(logN)で処理できる
import heapq

#1:普通に宣言
que = []

#2:pの先頭k項をキューにプッシュ
for i in range(k):
    heapq.heappush(que, p[i])

#pの先頭k項からなるキューの中でk番目に大きい値、
#すなわち最も小さい値はque[0]となる
print(que[0])

for i in range(k, n):
    heapq.heappush(que, p[i])
    #最小値をとりだす(棄てる)
    heapq.heappop(que)
    print(que[0])




