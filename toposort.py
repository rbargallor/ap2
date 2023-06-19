import yogi as yg
import heapq as pq

def solve(cua: list[int], g: list[list[int]], indegree: list[int]) -> list[int]:
	pq.heapify(cua)
	result=list()
	while cua:
		curr=pq.heappop(cua)
		result.append(curr)
		for neighbor in g[curr]:
			indegree[neighbor]-=1
			if indegree[neighbor] == 0:
				pq.heappush(cua, neighbor)

	return result

def main() -> None:
	for n in yg.tokens(int):
		m = yg.read(int)
		g = [list() for _ in range(n)]
		indegree = [0 for _ in range(n)]
		for _ in range(m):
			u, v = yg.read(int), yg.read(int)
			g[u].append(v)
			indegree[v]+=1
		source_nodes = [i for i in range(n) if indegree[i] == 0]
		
		result=solve(source_nodes, g, indegree)
		
		for i in range(n):
			if i != n-1:
				print(result[i], end=" ")
			else:
				print(result[i])

if __name__ == "__main__":
	main()