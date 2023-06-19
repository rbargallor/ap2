import yogi as yg
import typing as ty

Arbin = ty.Optional[tuple[str, 'Arbin', 'Arbin']]

def llegir_arbre() -> Arbin:
	
	x = yg.read(str)
	
	if x != "-1":
		return (x, llegir_arbre(), llegir_arbre())
	
	return None

def println(word: str, depth: int) -> None:
	print(" "*(10*depth-len(word)), word, sep="")

def write(tree: Arbin, depth: int) -> None:
	if tree is not None:
		write(tree[2], depth + 1)
		println(tree[0], depth)
		write(tree[1], depth + 1)

tree = llegir_arbre()

write(tree, 1)