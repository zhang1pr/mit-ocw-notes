# 1. Dictionary
Operations of the **Abstract Data Type**:  
* insert an item
* delete an item
* search item and return it with key if it exists

# 2. Hash Table
Uses an array indexed by keys to store items.

Steps:
1. reduce keys to non-negative integers - prehash
2. map integers to a hash table of size Θ(n) - hash

# 3. Chaining
If keys collide, chain them by **Linked List** in the slot of Hash Table.  
Search takes Θ(n) in worst-case.

# 4. Hash Function
**Division Method** - h(k) = k mod m, where m is prime and not too close to power of 2 or 10  
Division is slow.

**Multiplication Method** - h(k) = ((ak)mod(2^w))>>(w-r), where a is random and odd, k is w bits and m = 2^r  
Multiplication and bit extraction are faster than division.

**Universal Hashing** - h(k) = ((ak+b)mod(p))mod(m), where p is a large prime, a and b are random integers between 0 and p-1, and m is the number of slots  
The probablity of two keys colliding is 1/m, so the number of collisions with a key is n/m, which is **Load Factor**. If m = Θ(n), n/m = Θ(1).
