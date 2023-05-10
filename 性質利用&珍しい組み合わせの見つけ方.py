#abc249 d
#普通にやるとO(N^3)
#条件から読み取れること：AiはAjの倍数
#つまり、分母を決める→それの倍数(分子)を調べる
#というやり方でやればいい

from collections import Counter

N = int(input())
A = list(map(int, input().split()))

#これでAに整数xが現れる回数を数える
C = Counter(A)

ans = 0

A_max = 2 * 10 ** 5

for den in range(1, A_max + 1):
    for num in range(den, A_max + 1, den):
        #den:分母
        #num:分子(den飛ばしで探索)
        #k:Ak
        k = num // den
        #den, num, kがAにでてくる回数をかければ、
        #den, num, kの組み合わせが何通りあるかを調べれる
        ans += C[den] * C[num] * C[k]
print(ans)
