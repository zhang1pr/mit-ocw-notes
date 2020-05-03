# 1. Priority Queue
Operations of the **Abstract Data Type**:  
* insert an item
* return the item with largest (or smallest) key
* remove the item with largest (or smallest) key
* increase value of a key

# 2. Heap 
Is a nearly complete **Binary Tree** implemented in Array.

Positions:
* root index = 1  
* parent index = index/2  
* left child index = 2index  
* right child index = 2index + 1  

**Max-heap** (analogously for Min-heap)  
Every parent is greater than or equal to each of its children.

Operations of the **Data Structure**:
* max-heapify - Θ(log(n))
Correct a single violation of max-heap, bound by the tree height.
* build-max-heap - Θ(n)
Turn an unsorted array into a max-heap by iteratively calling max-heapify from second last level to the top.

# 3. Heap Sort 
**Heap Sort** - Θ(log(n))  
Initialize the heap:
1. call build-max-heap - Θ(n)

Iteratively extract the max n times:

2. swap the largest item from the beginning to the end of the array - Θ(1)
3. decrease heap size - Θ(1)
4. call max-heapify on the new root - Θ(log(n))  