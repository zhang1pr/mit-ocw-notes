# 1. Open Addressing
If keys collide, iteratively rehash the key until an empty slot is found, where hash function specifies the order of slots to probe.

The number of keys is smaller than or equal to the number of slots.

Operations:  
* insert - keep rehashing until an empty slot is found
* search - keep rehashing until key is found or an empty slot is found
  * if key is found, return true
  * else return false
* delete - keep rehashing until key is found or an empty slot is found
  * if key is found, replace it with a flag which is empty to **insert** and not to **search**
  * else return false

** Linear Probing** - h(k, i) = (h'(k)+i) mod m, where h'(k) is the ordinary hash function
Cluster of size Θ(log(n)) exists.

** Double Hashing** - h(k, i) = (h1(k)+i*h2(k)), where h1(k) and h2(k) are the ordinary hash functions, and h2(k) is relatively prime to m for all k
