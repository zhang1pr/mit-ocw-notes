# 1. Tree
The depth of a node is the number of edges from the root to the node.  
The height of a node is the number of edges from the node to the deepest leaf, also the larger height of its children plus 1.  
The height of a Tree is the height of the root.  
A full **Binary Tree** is a **Binary Tree** where each node has exactly zero or two children.  
A complete **Binary Tree** is a **Binary Tree** completely filled, with the possible exception of the bottom level filled from left to right.

# 2. AVL Tree
Requires heights of children of every node to differ by at most 1.

In worst case, where:
* n is the number of nodes in an AVL Tree
* N is the least number of nodes in an AVL Tree
* h is the height of the AVL Tree
N(1) = Θ(1)
N(h) = 1 + N(h-1) + N(h-2) > 2N(h-2) = Θ(2<sup>h/2</sup>)
=> h < 2log(n)
=> h = Θ(log(n))

Operation:
* rebalance - Θ(log(n))
  iteratively fix AVL property from changed node, where A is the lowest violating node and B is its right child,
  * if B is right heavy or balanced, right rotate A
  * else if B is left heavy, right rotate B and left rotate A
* insert - Θ(log(n))
  1. call **insert** from **Binary Search Tree** - Θ(log(n))
  2. call **rebalance** on the node - Θ(log(n))
* delete - Θ(log(n))
  1. call **delete** from **Binary Search Tree** - Θ(log(n))
  2. call **rebalance** on the parent of the node - Θ(log(n))

# 3. AVL Sort
**AVL Sort** - Θ(nlog(n)):
1. iteratively call **insert** on items - Θ(nlog(n))
2. do in-order travesal - Θ(n)
