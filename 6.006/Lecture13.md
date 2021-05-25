# 1. Graph
Consists of:
* V - a set of vertices
* E - a set of edges, unordered {v, w} or ordered (v, w)

In **Directed Graph**, the number of degrees is twice the number of edges.
In **Undirected Graph**, the number of in degrees and out degrees are equal, adding up to twice the number of edges.

# 2. Graph Data Structure
**Adjacency List** - Θ(V + E) space of words:  
An **Array** or a **Hash Table** contains **Linked List** of reachable vertices.

**Adjacency Matrix** - Θ(V<sup>2</sup>) space of bits:  
A 2D **Array** of all vertices contains 0 or 1.

# 2. Breadth First Search
Visits all vertices reachable from a given vertex V layer by layer, for **Directed Graph** and **Undirected Graph**.  
Parent pointers form a tree, where V is the root and any path from V to a vertex is a **Shortest Path**.  
Every edge is visited once in **Directed Graph**, twice in **Undirected Graph**.

**Breadth First Search** with **Adjacency List** - Θ(V + E)
