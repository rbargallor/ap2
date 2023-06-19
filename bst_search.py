import yogi as yg
import typing as ty

Arbin = ty.Optional[tuple[int, 'Arbin', 'Arbin']]

def llegir_arbre() -> Arbin:
	
	x = yg.read(int)
	
	if x != -1:
		return (x, llegir_arbre(), llegir_arbre())
	
	return None

def is_in_bst(x: int, tree: Arbin) -> bool:
	
	if tree is None:
		return False
	
	if x == tree[0]:
		return True

	if x < tree[0]:
		return is_in_bst(x, tree[1])
	else:
		return is_in_bst(x, tree[2])


ignorar = yg.read(int)
tree: Arbin = llegir_arbre()

for x in yg.tokens(int):
	print(x, 1 if is_in_bst(x, tree) else 0)