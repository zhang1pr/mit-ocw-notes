# 1. High Precision Multiplication
* Divide and Conquer - Θ(d<sup>2</sup>)
* Karatsuba - Θ(d<sup>log3</sup>) ≈ Θ(d<sup>1.584</sup>)  
  T(d) = 3T(d/2) + Θ(d)
* Toom-Cook - Θ(d<sup>log<sub>3</sub>5</sup>) ≈ Θ(d<sup>1.465</sup>)  
  T(d) = 5T(d/3) + Θ(d)
* Strassen - Θ(dlogd*loglogd)
* Furer - Θ(nlgn*2<sup>O(log<sup>\*</sup>n)</sup>), where O(log<sup>\*</sup>n) is iterated logarithm

# 2. High Precision Division
Steps to compute a/b:
1. computer ⌊R/b⌋, where R is large and easy to divide by, e.g. 2<sup>k<sup>
2. divide it by R and multiply it by a

In **Division** and **Newton's Method**, the number of digits precision starts out small and grows to d, so they have the same complexity as **Multiplication**.
