#abc 293 d
class UnionFind():
    def __init__(self,n):
        self.n = n
        self.parents = [-1] * n

    def find(self,x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x


    def same(self,x,y):
        return self.find(x) == self.find(y)
    

if __name__ == "__main__":
    N,M=[int(nm) for nm in input().split()]
    UF = UnionFind(N)
    x = 0

    for i in range(M):
        #C, Dは全部同じだから特に意識しなくていい
        A, B, C, D = input().split()
        A, C = int(A)-1, int(C) - 1

        #連結ならカウント
        if UF.same(A, C):
            x += 1

        #連結
        UF.union(A, C)

    y = 0

    #uf.parents[i]が負の場合、グラフの別の連結成分に属することを示します。したがって、 if uf.parents[i]<0:を使用して、グラフの別の連結成分の数をカウントします。
    for i in range(N):
        print(UF.parents[i])
        if UF.parents[i] < 0:
            y += 1
    
    print(x, y - x)