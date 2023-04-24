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

X, A, D, N = im()

#初項
first = A
#末項
last = A + (N - 1) * D


if first > last:
    first, last = last, first
    D = -D

#初項よりXが小さければ、
#初項からXを引いたものが答え
if X <= first:
    print(first - X)
#大きければ
elif last <= X:
    print(X - last)
else:
    r = (X - A) % D
    print(min(r, D - r))

