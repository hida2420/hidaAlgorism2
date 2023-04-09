N = int(input())
A=[int(a)-1 for a in input().split()]

called = [False for i in range(N)]

#N使わずにenumerate(A)でやれば、
#インデックスと要素同時に取り出せて一石二鳥
#計算量、コード量も減
for i, person in enumerate(A):
    if not called[i]:
        called[person] = True

sum = 0

not_called = []

for i in range(N):
    if called[i]:
        continue

    sum += 1
    not_called.append(i + 1)

print(sum)
print(*not_called)

