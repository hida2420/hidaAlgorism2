#にぶたん用ライブラリ
from bisect import*

#入力
n,q = map(int,input().split())
A = sorted(map(int,input().split()))

#累積和の計算
C = [0]*(n+1)
for i in range(n):
    C[i+1] = C[i]+A[i]


for _ in range(q):
    x = int(input())
    
    i = bisect_left(A,x)
    ans = (x*i-C[i])+((C[n]-C[i])-x*(n-i))
    print(ans)