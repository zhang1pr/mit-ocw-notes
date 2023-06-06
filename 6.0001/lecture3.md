# 1. String
String is an immutable sequence of case sensitive characters.  
Like numbers, strings can also be compared with comparison operators.

# 2. Find a root
* exhaustive enumeration
  guess every possible value
* approximation 
  guess every possible value with a small difference
* binary search
  guess in the left or right half of the search space each iteration
  * guess converges on the order of log(n) steps
  * works when value of function varies monotonically with input