import yogi

def bubble_up(i: int, heap: list[int]) -> None:

	if i == 0:
		return

	if heap[i//2] > heap[i]:
		heap[i//2], heap[i] = heap[i], heap[i//2]
		bubble_up(i//2, heap)

def bubble_down(i: int, heap: list[int], nodes: int) -> None:

	if i > nodes:
		return

	if heap[2*i] < heap[i] and heap[2*i]<heap[2*i+1]:
		heap[2*i], heap[i] = heap[i], heap[2*i]
		bubble_down(2*i, heap, nodes)
	elif heap[2*i + 1] < heap[i] and heap[2*i + 1]<heap[2*i]:
		heap[2*i + 1], heap[i] = heap[i], heap[2*i + 1]
		bubble_down(2*i + 1, heap, nodes)

def insert(n: int, heap: list[int], nodes: int) -> int:
	heap[nodes + 1] = n
	bubble_up(nodes + 1, heap)
	return nodes + 1

def pop(heap: list[int], nodes: int) -> int:
	minim = heap[1]
	heap[1] = heap[nodes]
	heap[nodes] = 0
	bubble_down(1, heap, nodes - 1)
	return minim

def main() -> None:
	nodes = 10
	min_heap = [0,13,21,16,24,31,19,68,65,26,33,0,0,0,0,0]
	nodes = insert(14, min_heap, nodes)
	print(pop(min_heap, nodes))
	print(min_heap)
main()