#にぶたん用ライブラリ
from bisect import*

#累積和の計算
#引数：累積和を求める配列、N
#例えば、1~3番目の要素の和を求める場合、C[3]-C[1]で求める
def CUSUM(A, n):
    C = [0]*(n+1)
    for i in range(n):
        C[i+1] = C[i]+A[i]
    return C

#入力
n,q = map(int,input().split())
A = sorted(map(int,input().split()))
#ここで得たコンパクトテクニック２つ
#１：[とりあえずソート]
# 　 こういう計算時にif文で
# 　 毎回大小比較する問題は、ソートするのが有効
#
#２：[愚直な操作を全部紙に書き出して式に表し、
# 　　その式に対して式変形を行う]
#　　同類項の整理などにより、下のansのような公式がみつかる

C = CUSUM(A, n)

for _ in range(q):
    x = int(input())
    
    #[bisect_left]
    #ソートされた配列Aの中で、xを挿入できる位置を探す
    #つまり、A[i] <= x < A[i+1]ってなるようなxの位置を探す(？) 
    i = bisect_left(A,x)
    ans = (x*i-C[i])+((C[n]-C[i])-x*(n-i))

    print(ans)