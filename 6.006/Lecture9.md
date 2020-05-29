# 1. Rehash
Steps:
1. initialize table of size - Θ(1)
2. build new hash function - Θ(1)
3. iteratively insert items from old table into new table by new hash function - Θ(n)

# 2. Resizable Array
When table is full, double the size; when table is only 1/4 full, halve the size.
Insertion to new table takes amortized Θ(1).

# 3. Rolling Hash ADT
Operations:
* add a character to the end
* skip the first character
* hash the list

# 4. Karp-Rabin Algorithm
**Karp-Rabin Algorithm** - Θ(|s|+|t|+m|s|), where s is short string, t is long string, and m is the number of matches

Steps:
1. hash s - Θ(|s|)
2. iteratively get **Rolling Hash** of |s| window in t, if two hashes match, compare substring in window with s - Θ(|t|-|s|+m|s|)
