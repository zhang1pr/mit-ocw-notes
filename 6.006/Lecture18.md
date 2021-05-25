# 1. Dijkstra Optimization
Optimizations that do not change worst-case time complexity:
* single target stop
stop when target is extracted from **Priority Queue**
* bi-directional search
    1. iteratively alternate forward **Dijkstra** from source and backward **Dijkstra** from target until a vertex has been extracted by both searches
    2. find a vertex with min **Shortest Path** weight sum to source and target
* A<sup>*</sup>
modify edge weights with potential function over vertices
