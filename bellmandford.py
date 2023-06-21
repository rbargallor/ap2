import yogi as yg

def bf(n: int, g: list[tuple[int,int,int]], x: int, y: int) -> int:
	d = [10**6 for _ in range(n)]

	d[x] = 0

	for _ in range(n-1):
		for u, v, w in g:
			if d[v] > d[u] + w:
				d[v] = d[u] + w
	return d[y]


def main() -> None:
	for n in yg.tokens(int):
		m = yg.read(int)	
		g = []
		
		for _ in range(m):
			u, v, w = yg.read(int),  yg.read(int),  yg.read(int)
			g.append((u,v,w))

		x, y = yg.read(int), yg.read(int)

		result = bf(n, g, x, y)

		if result == 10**6:
			print('no path from', x, 'to', y)
		else:
			print(result)

main()