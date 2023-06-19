import yogi
from collections import deque

def BFS(n: int, source: int, sink: int, parent: list[int], graph: list[list[int]], graph_matrix: dict[tuple[int, int],int]) -> bool:

	visited = [False]*n

	queue = deque()

	queue.append(source)
	visited[source] = True

	while queue:

		u = queue.popleft()

		for ind in graph[u]:
			if visited[ind] == False and graph_matrix.get((u,ind), 0) > 0:
				# If we find a connection to the sink node,
				# then there is no point in BFS anymore
				# We just have to set its parent and can return true
				queue.append(ind)
				visited[ind] = True
				parent[ind] = u
				if ind == sink:
					return True

	return False
		

def FordFulkerson(n: int, graph: list[list[int]], graph_matrix: dict[tuple[int, int],int], source: int, sink: int) -> int:

	# This array is filled by BFS and to store path
	parent = [-1]*n

	max_flow = 0

	while BFS(n, source, sink, parent, graph, graph_matrix):

		# Find minimum residual capacity of the edges along the
		# path filled by BFS. Or we can say find the maximum flow
		# through the path found.
		path_flow = 10**4
		s = sink
		while s != source:
			path_flow = min(path_flow, graph_matrix[(parent[s],s)])
			s = parent[s]

		# Add path flow to overall flow
		max_flow += path_flow

		# update residual capacities of the edges and reverse edges
		# along the path
		v = sink
		while v != source:
			u = parent[v]
			graph_matrix[(u,v)] -= path_flow
			if (v,u) not in graph_matrix:
				graph_matrix[(v,u)] = 0
			graph_matrix[(v,u)] += path_flow
			v = parent[v]

	return max_flow


for n in yogi.tokens(int):
	m = yogi.read(int)

	graph = [[] for _ in range(n)]
	graph_matrix = dict()

	for _ in range(m):
		u, v, c = yogi.read(int), yogi.read(int), yogi.read(int)
		graph_matrix[(u,v)] = c
		graph[u].append(v)
		graph[v].append(u)

	

	print(FordFulkerson(n, graph, graph_matrix, 0, n-1))
