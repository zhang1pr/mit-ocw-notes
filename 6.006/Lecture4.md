# 1. Priority Queue ADT
Operation:
* insert an item
* return the item with largest (or smallest) key
* remove the item with largest (or smallest) key
* increase value of a key

# 2. Heap
Is a nearly complete **Binary Tree** implemented by **Array**.

Positions:
* root index = 1
* parent index = index/2
* left child index = 2 * index
* right child index = 2 * index + 1

**Max-heap** (analogously for Min-heap)  
Every parent is greater than or equal to each of its children.

Operation of the **Data Structure**:
* max-heapify - Θ(log(n))
correct a single violation of max-heap, bound by the tree height
* build-max-heap - Θ(n)
turn an unsorted **Array** into a max-heap by iteratively calling **max-heapify** on nodes from second last level to the top

# 3. Heap Sort
**Heap Sort** - Θ(log(n)):
1. call **build-max-heap** - Θ(n)
2. iteratively extract the max - Θ(nlog(n))
    * swap the largest item from the beginning to the end of the **Array** - Θ(1)
    * decrease heap size - Θ(1)
    * call **max-heapify** on the new root - Θ(log(n))
