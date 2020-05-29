# 1. Newton's Method
Finds root of f(x) = 0 through successive approximation with quadratic convergence.

y = f(x<sub>i</sub>) + f'(x<sub>i</sub>)(x−x<sub>i</sub>), where x<sub>i+1</sub> is intercept on x-axis  
x<sub>i+1</sub> == (x<sub>i</sub> + a/x<sub>i</sub>)/2

# 2. Karatsuba's Mathod
T(n) = 3T(n/2) + Θ(n) = Θ(n<sup>log3</sup>) ≈ Θ(n<sup>log1.58</sup>)
