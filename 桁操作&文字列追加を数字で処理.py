MOD=998244353

#クエリ回数条件
M=600010

#p10:10^i、すなわち桁を表す
p10=[1]*M
for i in range(1,M):
    p10[i]=p10[i-1]*10%MOD

#初期設定
S=[1]
pos=0
val=1

#文字列ではなく数字として考える
Q=int(input())
for _ in range(Q):
    q=input()

    #クエリ1：数字の最後の桁にdを追加
    if q[0]=='1':
        d=int(q[2])
        S.append(d)
        val=(val*10+d)%MOD
    #クエリ2：
    elif q[0]=='2':

        #pos番目の要素を引く(先頭の文字を消す)
        L=len(S)-pos-1
        val=(val-S[pos]*p10[L])%MOD

        #次クエリ2が呼ばれたときに削除する場所
        pos+=1
    else:
        print(val)
