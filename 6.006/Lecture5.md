# 1. Runway Reservation System
Requires doing the following operations in O(log(n)) time:
* deletion
* search
* comparison
* insertion

Problems with the following Data Structures:
* unsorted Array - Θ(n) deletion, search and insertion
* sorted Array - Θ(n) deletion and insertion
* Linked List - Θ(n) search
* Heap - Θ(n) search
* Dictionary - Θ(n) search

# 2. Binary Search Tree
Every node is greater than or equal to its left child, and less than or equal to its right child.

Operations, where h is the height of the tree:
* search - Θ(h)
* insert - Θ(h)
  * **search** until an empty spot is found
* find-max, find-min - Θ(h):
  * return leftmost, rightmost child
* find-next-larger, find-next-smaller - Θ(h):
  * if target node has a right child, call **find-min** on the child
  * else if target node is a left child, return its parent
  * else if target node is a right child, go up until a parent is found on the right, return the parent
  * else target node has no successor because it's the largest item
* delete - Θ(h):
  * **search** and continue if node is found
  * if node has no child, **delete** it
  * if node has only a child, **delete** it and link its parent to its child in the same direction
  * if node has 2 children, call **find-next-larger**, **delete** the result node and assign its value to the original node

If Binary Search Tree is completely unbalanced and looks like a Linked List, h = Θ(n).

# 3. Augmented Binary Search Tree
Store subtree size in every node (or anything that takes Θ(1) for each node).

To count planes to land before time t, search until t is found - Θ(h):
* if t is found, add left subtree size + 1
* else if going left, do nothing
* else if going right, add left subtree size + 1

# 4. Data Structure
Operations include
* querys, e.g. find-max, find-min and search
* updates, e.g. insert and delete

**Representation Invariant**
is the precondition for a Data Stucture.