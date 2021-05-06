# 1. Depth First Search
Visits all vertices from a given vertex V by recursively doing **Depth First Search** on each neighbor vertex, for **Directed Graph** and **Undirected Graph**.  

**Depth First Search** with **Adjacency List** - Θ(V + E)

# 2. Edge Classification
* Tree Edge - to a new vertex (formed by **Depth First Search** tree)
* Forward Edge - to a descendant vertex
* Backward Edge - to an ancestor vertex 
* Cross Edge - to a sibiling vertex

**Undirected Graph** can only have **Tree Edge** and **Backward Edge**.

Graph has a cycle if and only if **Depth First Search** tree has a **Backward Edge**.

# 3. Topological Sort
Orders tasks by dependencies on a **Directed Acylic Graph**.  
One way is doing **Depth First Search** on vertice with 0 in degree and reversing vertex finishing times.
