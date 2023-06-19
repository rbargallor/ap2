from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Iterator, TypeVar, Generic, Optional, Callable

T = TypeVar('T')


@dataclass
class _Node(Generic[T]):
    """Internal node of a binary tree"""
    data: T
    left: Bintree[T]
    right: Bintree[T]


class Bintree(Generic[T]):
    _node: Optional[_Node[T]]

    def __init__(self, data: Optional[T] = None,
                 left: Optional[Bintree[T]] = None,
                 right: Optional[Bintree[T]] = None):
        if data is None:
            self._node = None
        else:
            if left is None:
                left = Bintree()
            if right is None:
                right = Bintree()
            self._node = _Node(data, left, right)

    @property
    def empty(self) -> bool:
        return self._node is None

    @property
    def data(self) -> T:
        assert self._node is not None
        return self._node.data

    @data.setter
    def data(self, v: T) -> None:
        assert self._node
        self._node.data = v

    @property
    def left(self) -> Bintree[T]:
        assert self._node
        return self._node.left

    @left.setter
    def left(self, t: Bintree[T]) -> None:
        assert self._node
        self._node.left = t

    @property
    def right(self) -> Bintree[T]:
        assert self._node is not None
        return self._node.right

    @right.setter
    def right(self, t: Bintree[T]) -> None:
        assert self._node
        self._node.right = t

    def size(self) -> int:
        return 0 if self.empty else 1 + self.left.size() + self.right.size()

    def num_levels(self) -> int:
        if self.empty:
            return 0
        return 1 + max(self.left.num_levels(), self.right.num_levels())

    def preorder(self) -> Iterator[T]:
        if not self.empty:
            yield self.data
            yield from self.left.preorder()
            yield from self.right.preorder()

    def levels(self) -> Iterator[T]:
        q: deque[Bintree[T]] = deque([self])
        while q:
            n = q.popleft()
            if not n.empty:
                q.append(n.left)
                q.append(n.right)
                yield n.data

    def visit_preorder(self, f: Callable[[T], T]):
        if not self.empty:
            self.data = f(self.data)
            self.left.visit_preorder(f)
            self.right.visit_preorder(f)

def build_expr(expr: str) -> Bintree:
    """Builds an expression tree from a correct
    expression represented in postfix notation"""
    # Create a list of all characters (without spaces)
    expr = [x for x in expr if not x.isspace()]
    stack: list[Bintree] = []
    for c in expr:
        if c.isalpha():
            # We have an operand. Create a leaf node
            stack.append(Bintree(c))
        else:
            # We have an operator (+ or *)
            right = stack.pop()
            left = stack.pop()
            stack.append(Bintree(c, left, right))
    # The stack has only one element: the root of the expression
    return stack.pop()

def infix_expr(t: Bintree) -> str:
    """Generates a string with the expression in
    infix notation"""
    if t.left.empty: # it is a leaf node (operand)
        return t.data
    # We have an operator. Add enclosing parenthesis (for safety)
    return '(' + infix_expr(t.left) + t.data + infix_expr(t.right) + ')'

def eval_expr(t: Bintree, v: dict[str, int]) -> int:
    """Evaluates an expression taking v as the value of the
    variables (e.g., v['a'] contains the value of a)"""
    if t.left.empty: # it is a leaf node: return the value
        return v[t.data]
    # We have an operator: evaluate subtrees and operate
    left = eval_expr(t.left, v)
    right = eval_expr(t.right, v)
    return left + right if t.data == '+' else left * right

t=build_expr('a b c * + d e * f + g * +')
print(infix_expr(t))
print(eval_expr(t, {'a':3, 'b':1, 'c':0, 'd':5,
'e':2, 'f':1, 'g':6}))

t_nodes=t.levels()

for nodes in t_nodes:
    print(nodes, end=" ")