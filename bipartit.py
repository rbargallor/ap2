import yogi as yg
from collections import deque

def bipartite(v: int, g: list[list[int]], c: list[int], n: int) -> tuple[bool, list[int]]:

	cua=deque()
	cua.append((v,-1))

	while cua:
		curr=cua.popleft()
		actual, ant = curr[0], curr[1]
		for neigh in g[actual]:
			if c[neigh] == -1:
				c[neigh] = 1-c[actual]
				cua.append((neigh,actual))
			elif c[neigh] == c[actual] and neigh != ant:
				return (False, c)
	return (True, c)


def main() -> None:
	for n in yg.tokens(int):
		m = yg.read(int)
		g = [list() for _ in range(n)]
		for _ in range(m):
			u, v = yg.read(int), yg.read(int)
			g[u-1].append(v-1)
			g[v-1].append(u-1)
		
		c = [-1 for _ in range(n)]

		posible = True

		for i in range(n):
			if c[i] == -1:
				result = bipartite(i, g, c, n)
				if result[0] == False:
					posible = False
					break
				c = result[1]
		
		print("yes" if posible else "no")


if __name__ == "__main__":
	main()