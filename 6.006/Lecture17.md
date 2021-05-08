# 1. Bellman-Ford
Problems of generic **Shortest Path** algorithm:
* time complexity can be exponential (even for positive edge weights)
* a negative cycle will make it run forever

**Bellman-Ford** - Θ(VE)
1. Relax all edges |V| - 1 times in a particular order - Θ(VE)
2. Relax all edges 1 time, report a negative cycle exists if any edge can be relaxed - Θ(E) 

**Longest Simple Path** and **Shortest Simple Path** are **NP-hard** problems.
**Bellman-Ford** does not work because it may report positive cycles (negated weights) for **Longest Simple Path** and negative cycles for **Shortest Simple Path**.
