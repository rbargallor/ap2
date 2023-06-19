from bintree import Bintree
from typing import TypeVar

T = TypeVar('T')

Coordinate = tuple[float,float]  # 2D coordinates (x,y)
Coordinates = dict[Bintree[T], Coordinate]  # Assign coordinates to each node

def draw(t: Bintree[T], width: float, height: float) -> Coordinates:
    """Given a tree t and a canvas of dimensions width*height, assuming
       that (0,0) is the upper-left corner, it assigns coordinates to the
       tree nodes in a way that no edges cross. The coordinates are returned
       as a result."""
    nodes = t.size()
    # Special cases: 0 or 1 nodes
    if nodes == 0:
        return {}

    if nodes == 1:
        # Put it in the middle of the canvas
        return {t: (width/2, height/2)}

    levels = t.num_levels()
    # x and y separation
    incx = width/(nodes-1)
    incy = height/(levels-1)
    c: Coordinates = {}  # Dictionary including the coordinates
    draw_rec(t, 0, incx, 0, incy, c)
    return c

def draw_rec(t: Bintree[T], x: float, incx: float, y: float, incy: float,
             c: Coordinates) -> float:
    """Assigns coordinates to the subtree rooted at t, using (x,y) as the
       coordinates of the upper-left corner and using incx and incy as the
       displacement for each node (visited in in-order). It returns the
       value of the x coordinate for the following node in the tree."""
    # Basic case (empty tree, nothing to do)
    if t.empty:
        return x
    # In-order traversal of the left tree (x is updated accordingly)
    x = draw_rec(t.left, x, incx, y+incy, incy, c)
    # Assign coordinates to the root of the subtree and increase x
    c[t] = (x, y)
    x += incx
    # In-order traversal of the right tree (x is updated accordingly and returned)
    return draw_rec(t.right, x, incx, y+incy, incy, c)

def main():
    """Test for drawing a tree.
                 A
               /   \
              B     C
             / \   /
            D   E F
           / \   \
          G   H   I
    """
    # The leaves
    tg: Bintree[str] = Bintree('G')
    th: Bintree[str] = Bintree('H')
    ti: Bintree[str] = Bintree('I')
    tj: Bintree[str] = Bintree('J')
    tk: Bintree[str] = Bintree('K')
    # The internal nodes
    td: Bintree[str] = Bintree('D', tg, th)
    te: Bintree[str] = Bintree('E', None, ti)
    tb: Bintree[str] = Bintree('B', td, te)
    tf: Bintree[str] = Bintree('F', tj, tk)
    tc: Bintree[str] = Bintree('C', tf)
    t: Bintree[str] = Bintree('A', tb, tc)

    # Assign coordinates in a canvas of size 5x6
    coord = draw(t, 5, 6)

    # Print the coordinates
    for t, c in coord.items():
        print(t.data, c)

main()
