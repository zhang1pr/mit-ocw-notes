# 1. Computational Complexity
* P (Polynomial) - problems solvable in polynomial (n<sup>c</sup>) time
* NP (Nondeterministic Polynomial) - problems verifiable in polynomial (n<sup>c</sup>) time
* EXP (Exponential) - problems solvable in exponential (2<sup>n<sup>c</sup></sup>) time
* R (Recursive) - problems solvable in finite time

Most problems are uncomputable.

If the input size is doubled, running time will grow linearly for **P** and quadratically for **EXP**.

# 2. Hardness and Completeness
* NP-hard - problems as hard as every problem in **NP**
* NP-complete - problems in boths **NP** and **NP-hard**

# 3. Reduction
Convert the original problem into a problem whose solution is known

**NP-complete** problems are all interreducible by polynomial-time reductions so their NP-hardness can be proved.
