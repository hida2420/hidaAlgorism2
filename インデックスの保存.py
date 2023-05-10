import numpy as np
N, Q = map(int, input().split())
A = list(range(N + 1))  # 1はじまりにするためにN+1の長さで作る、A[0]は使わない
idx = list(range(N + 1))  # iの書かれたボールははじめi番目にある

#インデックスを要素と同時にとりだすのではなく、
#インデックスを保存するリスト(idx)を用いて操作を行う
for _ in range(Q):
    x = int(input())
    first_i = idx[x]  # xの位置
    second_i = first_i + 1 if first_i != N else first_i - 1  # 通常は右隣のボールと入れ替えるが、右端なら左隣と入れ替える
    y = A[second_i]  # 入れ替えるボールに書かれた数
    A[first_i], A[second_i] = A[second_i], A[first_i]  # スワップ
    idx[x] = second_i  # xはsecond_i、yはfirst_iに移動
    idx[y] = first_i
print(*A[1:])  # A[0]を出力しないよう注意
