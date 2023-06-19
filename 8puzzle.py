import yogi as yg
import heapq
from dataclasses import dataclass

@dataclass

class state:
	grid: list[list[int]]
	g: int
	f: int
	zero_pos: tuple[int,int]

	def __lt__(self, other):
		return self.f < other.f

def goal_position(n: int) -> tuple[int,int]:
	real_grid=[[1,2,3],[4,5,6],[7,8,0]]

	for i in range(3):
		for j in range(3):
			if real_grid[i][j]==n:
				return (i,j)

def h(grid: list[list[int]]) -> int:
	diff = 0
	for r in range(3):
		for c in range(3):
			gr, gc = goal_position(grid[r][c])
			diff += abs(r-gr) + abs(c-gc)

	return diff

def inv_count(grid: list[list[int]]) -> bool:
	total = 0
	grid_array = [num for row in grid for num in row]
	for i in range(9):
		for j in range(i+1, 9):
			if grid_array[j] != 0 and grid_array[i] != 0 and grid_array[i]>grid_array[j]:
				total+=1
	return total

def posible(r: int, c: int) -> bool:
	return 0<=c<3 and 0<=r<3

def state_str(grid: list[list[int]]) -> str:
	grid_array = [num for row in grid for num in row]
	return ''.join(str(e) for e in grid_array)

def solve(initial_state: state) -> int:
	
	pq = []

	directions=[(1,0),(0,1),(-1,0),(0,-1)]

	initial_zero_pos_r, initial_zero_pos_c = initial_state.zero_pos[0], initial_state.zero_pos[1]

	processed_states: dict[str, int] = dict()

	heapq.heappush(pq, (initial_state.f, initial_state))

	while pq:

		curr_state = heapq.heappop(pq)[1]

		if curr_state.f == curr_state.g:
			return curr_state.g
		print(curr_state)
		
		for dr, dc in directions:

			grid = [row[:] for row in curr_state.grid]
			g = curr_state.g
			f = curr_state.f
			zero_pos = curr_state.zero_pos

			curr_row, curr_col = zero_pos[0], zero_pos[1]

			if posible(curr_row + dr, curr_col + dc):
				g = g + 1
				grid[curr_row][curr_col], grid[curr_row + dr][curr_col + dc] = grid[curr_row + dr][curr_col + dc], grid[curr_row][curr_col]
				zero_pos = (curr_row + dr, curr_col + dc)
				f = g + h(grid)
				new_state = state(grid, g, f, zero_pos)

				if state_str(grid) not in processed_states or processed_states[state_str(grid)] < g:
					processed_states[state_str(grid)] = g
					heapq.heappush(pq, (new_state.f, new_state))



def main() -> None:
	grid=[[yg.read(int) for _ in range(3)] for _ in range(3)]
	for r in range(3):
		for c in range(3):
			if grid[r][c] == 0:
				zero_pos = (r,c)

	zero_row, zero_col = zero_pos[0], zero_pos[1]

	initial_state = state(grid, [[100 for _ in range(3)] for _ in range(3)], [[100 for _ in range(3)] for _ in range(3)], zero_pos)
	initial_state.g = 0
	initial_state.f = h(grid)

	if inv_count(grid) % 2 == 1:
		print(None)
	else:
		print(solve(initial_state))


			
if __name__ == "__main__":
	main()