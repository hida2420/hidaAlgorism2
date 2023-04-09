#abc294c
N,M=[int(nm) for nm in input().split()]
A=[[int(a),i+1] for i,a in enumerate(input().split())]
B=[[int(b),-(i+1)] for i,b in enumerate(input().split())]

C = sorted(A+B)

ans_A = [0 for i in range(N)]
ans_B = [0 for i in range(M)]

#iが0より大きい→Aの要素
#それ以外はBの要素
for j, (c, i) in enumerate(C):
    if i > 0:
        ans_A[i - 1] = j + 1
    else:
        ans_B[-i-1] = j + 1

print(*ans_A)
print(*ans_B)