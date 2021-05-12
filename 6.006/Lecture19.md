# 1. Dynamic Programming
Is an algorithmic design technique that re-uses solutions to subproblems to solve problem, where subproblem dependency should be acyclic. **Dynamic Programming** can be viewed as finding **Shortest Path** in subproblem dependency **Directed Acyclic Graph**.

* Top-down  
combines recursion and memoization of subproblem
* Bottom-up  
follows topological sort of subproblem dependency **Directed Acyclic Graph**

Bottom-up approach is faster and uses less space than top-down approach because it doesn't use recursion.
