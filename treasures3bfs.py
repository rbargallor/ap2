import yogi as yg
from collections import deque

def posible(n:int, m:int, graph: list[list[str]],visited:list[list[bool]] ,r: int, c: int) -> bool:
	return 0<=c<m and 0<=r<n and graph[r][c]!='X' and not visited[r][c]

def solve(n: int, m: int, g: list[list[str]], v: list[list[bool]], ri: int, ci: int) -> int:
	cua=deque()
	directions=[(1,0),(0,1),(-1,0),(0,-1)]
	total=0
	v[ri][ci] = True
	cua.append((ri,ci))
	while cua:
		curr=cua.popleft()
		r, c=curr[0], curr[1]
		for dr,dc in directions:
			if posible(n,m,g,v,r+dr,c+dc):
				v[r+dr][c+dc] = True
				cua.append((r+dr,c+dc))
				if g[r+dr][c+dc] == 't':
					total+=1
	return total



def main()->None:
	n,m=yg.read(int),yg.read(int)
	graph=[[c for c in yg.read(str)] for i in range(n)]
	visited=[[False for j in range(m)] for i in range(n)]
	ri,ci=yg.read(int)-1,yg.read(int)-1
	print(solve(n,m,graph,visited,ri,ci))

if __name__=="__main__":
	main()