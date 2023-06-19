import yogi as yg
from dataclasses import dataclass
from collections import deque

@dataclass
class Rock:
	x:float
	y:float
	r:float
	def __init__(self,x,y,r)->None:
		self.x=x
		self.y=y
		self.r=r

def put_edge(rock1:Rock, rock2:Rock, d:float)->bool:
	return (rock1.x-rock2.x)**2+(rock1.y-rock2.y)**2<=(d+rock1.r+rock2.r)**2


def minimum_jumps(n: int,d:float)->int:
	rocks=[Rock(yg.read(float),yg.read(float),yg.read(float)) for _ in range(n)]
	dist=[-1 for _ in range(n)]
	cua: deque[int]=deque()
	cua.append(0)
	dist[0]=0
	while len(cua)>0:
		actual=cua.popleft()
		if actual==n-1:
			break
		for i,rock in enumerate(rocks):
			if dist[i]==-1 and put_edge(rocks[actual],rock,d):
				dist[i]=dist[actual]+1
				cua.append(i)
	return dist[-1]


def main():
	for n in yg.tokens(int):
		d=yg.read(float)

		result=minimum_jumps(n,d)

		if result==-1:
			print("Xof!")
		else: print(result)
	

if __name__=="__main__":
	main()