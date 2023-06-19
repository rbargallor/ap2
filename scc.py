import yogi as yg


def order(v:int, g: list[list[int]], visited: list[bool], result: list[int]) -> list[bool]:
	visited[v] = True
	for neighbor in g[v]:
		if not visited[neighbor]:
			order(neighbor, g, visited, result)
	result.append(v)

	return visited

def reverse_graph(n: int, g: list[list[int]]) -> list[list[int]]:
	gr = [list() for _ in range(n)]

	for u in range(n):
		for v in g[u]:
			gr[v].append(u)

	return gr

def dfs(v: int, g: list[list[int]], visited: list[bool]) -> list[bool]:

	visited[v] = True
	for neigh in g[v]:
		if not visited[neigh]:
			dfs(neigh, g, visited)
	return visited


def main() -> None:
	t = yg.read(int)

	for it in range(t):
		n, m = yg.read(int), yg.read(int)
		g = [list() for _ in range(n)]
		
		for _ in range(m):
			u, v = yg.read(int), yg.read(int)
			g[u].append(v)
	
		visited = [False for _ in range(n)]
		result= list()

		for i in range(n):
			if not visited[i]:
				visited = order(i, g, visited, result)

	
		reverse_g = reverse_graph(n, g)


		count = 0

		visited = [False for _ in range(n)]

		for i in reversed(result):
			if not visited[i]:
				count += 1
				visited = dfs(i, reverse_g, visited)
		
		print("Graph #"+str(it+1)+" has "+str(count)+" strongly connected component(s).")


			
if __name__ == "__main__":
	main()