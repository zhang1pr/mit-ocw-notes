# 1. Binary Search Tree
Every node is greater than or equal to its left child, and less than or equal to its right child.

Operation, where h is the height of the tree:
* search - Θ(h)
* insert - Θ(h)
  * call **search** until an empty slot is found
* find-max, find-min - Θ(h)
  * return leftmost, rightmost child
* find-next-larger, find-next-smaller - Θ(h)
  * if target node has a right child, call **find-min** on the child
  * else if target node is a left child, return its parent
  * else if target node is a right child, go up until a parent is found on the right, return the parent
  * else target node has no successor because it's the largest item
* delete - Θ(h)
  * call **search** and continue if node is found
  * if node has no child, call **delete** on it
  * if node has only a child, call **delete** on it and link its parent to its child in the same direction
  * if node has 2 children, call **find-next-larger**, call **delete** on the result node and assign its value to the original node

If a **Binary Search Tree** is completely unbalanced as a **Linked List**, h = Θ(n).

Cost of deletion, searching and insertion:
* unsorted Array - Θ(n) deletion, search and insertion
* sorted Array - Θ(n) deletion and insertion
* Linked List - Θ(n) search
* Heap - Θ(n) search
* Dictionary - Θ(n) search

# 2. Augmented Binary Search Tree
Stores subtree size in every node (or anything that takes Θ(1) for each node).

To count planes to land before time t, search until t is found - Θ(h):
* if t is found, add left subtree size + 1
* else if going left, do nothing
* else if going right, add left subtree size + 1

# 3. Data Structure
Operation:
* querys, e.g. find-max, find-min and search
* updates, e.g. insert and delete

**Representation Invariant**  
Is the precondition for a Data Stucture.
