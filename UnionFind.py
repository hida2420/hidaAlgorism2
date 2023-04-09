class UnionFind:
    def __init__(self,n):
        self.n=n
        self.parent_size=[-1]*n
    def leader(self,a):
        if self.parent_size[a]<0: return a
        self.parent_size[a]=self.leader(self.parent_size[a])
        return self.parent_size[a]
    def merge(self,a,b):
        x,y=self.leader(a),self.leader(b)
        if x == y: return
        if abs(self.parent_size[x])<abs(self.parent_size[y]):x,y=y,x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y]=x
    def same(self,a,b):
        return self.leader(a) == self.leader(b)
    def size(self,a):
        return abs(self.parent_size[self.leader(a)])
    def groups(self):
        result=[[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]
    def ufprint(self):
        result=[[] for _ in range(self.n)]
        ans = []
        for i in range(self.n):
            result[self.leader(i)].append(i)
        for i in range(1, self.n):
            for j in reversed(result[i]):
                ans.append(j)
        print(*ans)



N, M = map(int, input().split())
A=[int(a) for a in input().split()]
UF = UnionFind(N+1)
for i in range(M):
    UF.merge(A[i], A[i]+1)
UF.ufprint()



