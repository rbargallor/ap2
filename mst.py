import yogi as yg

def find(x: int, parent: list[int]) -> int:
	if x == parent[x]:
		return x
	parent[x] = find(parent[x], parent)

	return parent[x]

def join(x: int, y: int, parent: list[int], rank: list[int]) -> None:
	x_parent = find(x, parent)
	y_parent = find(y, parent)
	if x_parent == y_parent:
		return
	
	if rank[x_parent] > rank[y_parent]:
		parent[y_parent] = x_parent
		rank[y_parent] = rank[x_parent]
	elif rank[x_parent] < rank[y_parent]:
		parent[x_parent] = y_parent
		rank[x_parent] = rank[y_parent]
	else:
		parent[y_parent] = x_parent
		rank[y_parent]+=1

def mst(edge_list: list[tuple[int,int,int]], rank: list[int], parent: list[int]) -> int:
	edge_list.sort(key=lambda x:x[2])
	result=0
	for u, v, w in edge_list:
		if find(u, parent) != find(v, parent):
			join(u, v, parent, rank)
			result += w
	return result


def main() -> None:
	for n in yg.tokens(int):
		m = yg.read(int)
		edge_list = list()
		for _ in range(m):
			u, v, w = yg.read(int), yg.read(int), yg.read(int)
			edge_list.append((u-1,v-1,w))
		rank = [1 for _ in range(n)]
		parent = [i for i in range(n)]
		print(mst(edge_list, rank, parent))


if __name__ == "__main__":
	main()