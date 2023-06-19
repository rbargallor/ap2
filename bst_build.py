import yogi as yg
import typing as ty

Arbin = ty.Optional[tuple[int, 'Arbin', 'Arbin']]

def insert_element(n: int, tree: Arbin) -> Arbin:

	if tree is None:
		return (n, None, None)

	if n < tree[0]:
		return (tree[0], insert_element(n, tree[1]), tree[2])
	elif n > tree[0]:
		return (tree[0], tree[1], insert_element(n, tree[2]))

def pre_order(tree: Arbin) -> None:

	if tree is not None:
		print(tree[0])
		pre_order(tree[1])
		pre_order(tree[2])
	
list_num = list()

for n in yg.tokens(int):
	list_num.append(n)

s: set = set()

tree: Arbin = (list_num[0], None, None)
s.add(list_num[0])

for i in range(1, len(list_num)):
	if list_num[i] not in s:
		tree = insert_element(list_num[i], tree)
		s.add(list_num[i])

pre_order(tree)


