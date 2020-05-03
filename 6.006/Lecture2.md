# 1. Models of Computation
Specifies:  
* available operations
* cost of each operation
* cost of algorithm - sum of operation costs

**Random Access Machine** - Array

**Pointer Machine** - Linked List
Can be implemented on Random Access Machine.

# 2. Python Model
* list - Array
* tuple, str - Linked List
* dict - Hash Table
* set - Hash Set
* headq - Heap

# 3. Document Distance
**Document Length** is the number of the words in the document.

**Dot Product** of 2 documents is sum of the product of each word occurrence count in both documents.

**Document Distance** of 2 documents is arccosine value of their **Dot Product** divided by each **Document Length**.