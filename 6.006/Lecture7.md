# 1. Decision Tree
Represents all possible comparisons, outcomes and answers in Comparsion Model, where:
* internal node = comparison
* leaf = answer
* root-to-leaf path = algorithm execution
* path length = running time
* height of tree = worst-case running time

# 2. Comparison model
The number of comparsions is the time cost.

**Searching** - Ω(log(n))

**Sorting** - Ω(nlog(n))  
log(n!) = log(2πn<sup>1/2</sup>(n/e)<sup>n</sup>) = nlog(n) by **Sterling's Formula**

# 3. Linear-time Sorting
For k = n<sup>Θ(1)</sup>, n keys from 0 to k-1 can be sorted in Θ(n) time.

**Counting Sort** - Θ(n+k), where k is the number of keys

**Radix Sort** - Θ((n+b)log<sub>b</sub>k), where k is the number of keys and b is the base  
Iteratively sort by least significant digit by calling **Counting Sort**.

When b = Θ(n) and k <= n<sup>c</sup>, Θ((n+b)log<sub>b</sub>k) = Θ(n).

# 4. Stable Sort
Requires elements with the same key to keep the same order.

* Insertion Sort ✅  
* Merge Sort ✅
* Heap Sort ❌
* AVL Sort ✅
* Counting Sort ✅
* Radix Sort ✅

Radix Sort assumes sorting each digit is stable.
