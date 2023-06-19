import yogi as yg
import typing as ty


Arbin = ty.Optional[tuple[int, 'Arbin', 'Arbin']]

def llegir_arbre() -> Arbin:
	
	x = yg.read(int)
	
	if x != -1:
		return (x, llegir_arbre(), llegir_arbre())
	
	return None

def post_order(tree: Arbin) -> None:

	sol: str = ""

	if tree is not None:
		sol += str(post_order(tree[1])) + str(post_order(tree[2])) + " " + str(tree[0])
	
	return sol

def in_order(tree: Arbin) -> None:

	sol: str = ""

	if tree is not None:
		sol += str(in_order(tree[1])) + " " + str(tree[0]) + str(in_order(tree[2])) 
	
	return sol	


tree: Arbin = llegir_arbre()
print("pos:", post_order(tree), sep="")
print("ino:", in_order(tree), sep="")