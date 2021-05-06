# 1. Shortest Path
* Directed Acyclic Graph  
**Topological Sort** - Θ(V + E)
Relax edges in topological order

* Non-negative Weighted Graph  
**Dijkstra** - Θ(Vlog(V) + Elog(V))/Θ(Vlog(V) + E)  
Iteratively select the non-visited and discovered vertex with min distance from source vertex, discover new vertice and relax edges

# 2. Dijkstra
Operation:
* Θ(V) * insert a vertex 
* Θ(V) * extract the non-visited and discovered vertex with min distance
* Θ(E) * decrease a vertex's distance

Implementation:
**Array** - Θ(V<sup>2</sup> + E)
* Θ(V) * Θ(1)
* Θ(V) * Θ(V)
* Θ(E) * Θ(1)

**Min Heap** - Θ(Vlog(V) + Elog(V))
* Θ(V) * Θ(log(V))
* Θ(V) * Θ(log(V))
* Θ(E) * Θ(log(V))

**Fibonacci Heap** - Θ(Vlog(V) + E)
* Θ(V) * Θ(log(V))
* Θ(V) * Θ(log(V))
* Θ(E) * amortized Θ(1)
