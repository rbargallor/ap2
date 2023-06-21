import yogi as yg
import heapq as hp

def dijkstra(n: int, g: list[list[int]], x: int, y: int) -> int:
	
	d = [-1 for _ in range(n)]

	d[x] = 0

	pq = []

	hp.heappush(pq, (0, x))

	while pq:

		dist, curr = hp.heappop(pq)

		if curr == y:
			return d[y]

		if d[curr] < dist:
			continue

		for weight, neigh in g[curr]:
			if d[neigh]==-1 or d[neigh] > d[curr] + weight:
				d[neigh] = d[curr] + weight
				hp.heappush(pq, (d[neigh], neigh))

	return d[y]


def main() -> None:
	for n in yg.tokens(int):
		m = yg.read(int)	
		g = [list() for _ in range(n)]
		
		for _ in range(m):
			u, v, w = yg.read(int),  yg.read(int),  yg.read(int)
			g[u].append((w,v))

		x, y = yg.read(int), yg.read(int)

		result = dijkstra(n, g, x, y)

		if result == -1:
			print('no path from', x, 'to', y)
		else:
			print(result)

if __name__ == "__main__":
	main()