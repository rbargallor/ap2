import yogi as yg
from collections import deque

def state_list(n: int, capacity: list[int], current: list[int], visited: dict[tuple,bool]) -> list[list[int]]:

	states=[]

	for i in range(n):
		for j in range(n):
			if i!=j:
				curr_cpy = current[:]
				original_j = curr_cpy[j]
				curr_cpy[j] = min(curr_cpy[j] + curr_cpy[i], capacity[j])
				curr_cpy[i] = max(0, curr_cpy[i] - abs(curr_cpy[j] - original_j))

				if curr_cpy[i] > capacity[i] or curr_cpy[j] > capacity[j]:
					continue

				state = tuple(curr_cpy)

				if  state not in visited:
					visited[state] = True
					states.append(curr_cpy)
	return states

def correct(n: int, current: list[int], obj: list[int]) -> bool:
	for i in range(n):
		if obj[i] != -1 and current[i] != obj[i]:
			return False
	return True

def solve(n: int, capacity: list[int], current: list[int], obj: list[int]) -> int:
	dq = deque()
	dq.append((0,current))

	visited = dict()

	while dq:

		curr_steps, curr_state = dq.popleft()

		for state in state_list(n, capacity, curr_state, visited):
			if correct(n, state, obj):
				return curr_steps + 1

			dq.append((curr_steps + 1, state))

	return -1



def main() -> None:
	n = yg.read(int)
	capacity = [yg.read(int) for _ in range(n)]
	current = [yg.read(int) for _ in range(n)]
	obj = [yg.read(int) for _ in range(n)]
	print(solve(n, capacity, current, obj))

main()