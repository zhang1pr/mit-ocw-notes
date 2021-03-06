# 1. 1D Peak Finding
A peak always exists in any **Array** when defined as an item greater than or equal to neighbours.

**Brute Force** - Θ(n)  
Scan through the **Array**.

**Divide and Conquer** - Θ(log(n))  
Recursively choose the middle point of the **Array**,
* if it's smaller than left neighbour, move left
* else if it's smaller than right neightbour, move right
* else return the middle point

T(1) = Θ(1)
T(n) = T(n/2) + Θ(1) = log(n) * Θ(1) = Θ(log(n))

# 2. 2D Peak Finding
Find a 2D peak in a MxN matrix.

**Brute Force** - Θ(mn)  
Greedy Ascent algorithm

**Wrong Divide and Conquer** - Θ(log(m)log(n)):  
1. find a 1D peak on middle column at row i
2. find a 1D peak on row i

It's wrong because a 2D peak may not exist on row i but exist on other rows.

**Correct Divide and Conquer** - Θ(nlog(m))  
Resursively find global max on the middle column,
* if it's smaller than left neighbour, move left
* else if it's smaller than right neightbour move right
* else the max is the 2D peak

T(1) = Θ(n)
T(n, m) = T(n, m/2) + Θ(n) = log(m) * Θ(n) = Θ(nlog(m))

# 3. Asymptotic Complexity
If g(x) = Θ(f(x)), they only differ by a constant factor.

log(n) has an implicit base 2 in Computer Science.

log(n<sup>100</sup>) = 100log(n) = Θ(log(n))
log<sub>5</sub>n = log(n)/log(5) = Θ(log(n))
log(100n) = log(100) + log(n) = Θ(log(n))
log(C(n, n/2)) = log(2<sup>n</sup>/n<sup>1/2</sup>) = nlog2 = Θ(n)
