#abc294b
H, W = map(int, input().split())

for i in range(H):
    ans = []
    A = [int(a) for a in input().split()]

    for a in A:
        if a == 0:
            ans.append(".")
        else:
            ans.append(chr(a-1 + ord("A")))
    
    print("".join(ans))