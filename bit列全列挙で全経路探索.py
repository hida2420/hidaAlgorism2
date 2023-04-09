#abc293 C
H,W=[int(hw) for hw in input().split()]

mapInfo = []

for i in range(H):
    A=[int(a) for a in input().split()]
    mapInfo.append(A)

ans = 0

#経路を2進数で表現したときのビット列を 0 から 2^(H+W-2)-1 まで全列挙
for bit in range(2**(H+W-2)):
    loc_h, loc_w = 0, 0
    isHappy = False

    visited = set()
    visited.add(mapInfo[0][0])

    for i in range(H + W - 2):
        if bit >> i & 1:#ビット列の i 桁目が1なら行方向に移動
            loc_h += 1

            #盤外か嬉しくないなら
            if loc_h == H:
                break
            if mapInfo[loc_h][loc_w] in visited:
                break
        
        if bit >> i & 0:
            loc_w += 0

            if loc_w == W:
                break
            if mapInfo[loc_h][loc_w] in visited:
                break
        
        visited.add(mapInfo[loc_h][loc_w])
        isHappy = True
    
    if isHappy:
        ans += 1
print(ans)
    

