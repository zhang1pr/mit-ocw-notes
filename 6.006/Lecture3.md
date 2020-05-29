# 1. Sorting
Strategies to have a sorted array:  
* sort the array by a sorting algorithm
* maintain a sorted array as more items are coming

Benefits if array is sorted:
* find median - middle point access - Θ(1)
* find an item - binary search - Θ(log(n))
* find duplicates - linear search - Θ(n) in-place

**Insertion Sort** - Θ(n<sup>2</sup>)
Iteratively insert the smaller item down to the correct position by pairwise swap.

**Binary Insertion Sort** - Θ(n<sup>2</sup>)  
If we replace pairwise swap with binary search, we reduce compare from Θ(n<sup>2</sup>) to Θ(nlog(n)) but keep insertion Θ(n<sup>2</sup>) because of shifting items.

**Merge Sort** - Θ(nlog(n))
Recursively split and merge back.

Split represents **Divide and Conquer** - Θ(1)  
Merge uses **Two Pointers Techique** - Θ(n)

T(1) = Θ(1)  
T(n) = 2T(n/2) + Θ(n) = 2(2T(n/4) + n/2) + n = 4T(n/4) + 2n = nT(1) + nlog(n) = Θ(nlog(n))

**In-place Sort**  
Requires Θ(1) auxiliary space.

Insertion Sort requires Θ(1) auxiliary space.✅  
Traditional Merge Sort requires Θ(n) auxiliary space during merge.❌

In-place Merge Sort requires Θ(1) auxiliary space but has much worse Θ(nlog(n)) running time.
