#入力受取
n = int(input())

#{}で辞書になる
#多分defaultdictと同じ
#このコードは愚直なTLEコード(下に記載)を
#辞書に変えただけ
#これだけで実行時間半分イカになった
count = {}
for _ in range(n):
    S = input()
    if S not in count:
        print(S)
        count[S] = 1
    else:
        print(f"{S}({count[S]})")
        count[S] += 1

#slist = []
#n = ii()
#for j in range(n):
#    s = i()
#    if not s in slist:
#        slist.append(s)
#        print(s)
#    else:
#        print("{}({})".format(s, slist.count(s)))
#        slist.append(s)