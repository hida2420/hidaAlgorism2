count = [0 for i in range(2<<17)]
N = int(input())

#AB = X, CD = Yとして、X+Y = Nを考える
#Xを1～Nで全探索→Y = N - Xとわかる
#Xを全探索してYを固定
#これは調和級数→計算量はO(NlogN)
#N//Aが範囲なのは、A*B <= N のBを以降してるから
#約数の個数を数えている
for A in range(1, N+1):
    for B in range(1, N//A+1):
        count[A*B] += 1

ans = 0

for i in range(1, N):
    
    #Y = N - Xの利用

    print(count[i])
    ans += count[i] * count[N-i]

#print(ans)