# Algorithm Complexity Analysis

Understanding time and space complexity is crucial for evaluating and comparing algorithms. This guide explains Big O notation and how to analyze algorithms.

---

## Big O Notation

### What is Big O?
Big O notation describes the upper bound of an algorithm's growth rate as the input size approaches infinity. It helps us understand how an algorithm scales.

### Common Classes (Ordered by Efficiency)

| Notation | Name | Description | Example |
|----------|------|-------------|---------|
| O(1) | Constant | Time doesn't change with input size | Accessing array by index |
| O(log n) | Logarithmic | Time grows slowly as input doubles | Binary search |
| O(√n) | Square Root | Time grows as square root of input | Jump search |
| O(n) | Linear | Time grows proportionally with input | Linear search |
| O(n log n) | Linearithmic | Slightly worse than linear | Merge sort, quicksort |
| O(n²) | Quadratic | Time grows with square of input | Bubble sort, nested loops |
| O(n³) | Cubic | Triple nested loops | Matrix multiplication |
| O(2ⁿ) | Exponential | Time doubles with each addition | Recursive Fibonacci |
| O(n!) | Factorial | Permutations of n items | Traveling salesman (brute force) |

### Growth Rate Visualization

```
Elements | O(1) | O(log n) | O(n) | O(n log n) | O(n²)
---------|------|----------|------|------------|------
10       | 1    | 3        | 10   | 30         | 100
100      | 1    | 7        | 100  | 700        | 10,000
1,000    | 1    | 10       | 1,000| 10,000     | 1,000,000
1,000,000| 1    | 20       | 10⁶  | 20×10⁶     | 10¹²
```

---

## How to Analyze Time Complexity

### 1. Count Basic Operations
Identify the most frequent operation and count how many times it executes.

### 2. Identify Loops
- **Single loop:** Typically O(n)
- **Nested loops:** Multiply complexities (e.g., two nested O(n) loops = O(n²))
- **Loop with halving:** Typically O(log n)

### 3. Analyze Recursion
- **Recursive calls:** Count how many times function calls itself
- **Divide and conquer:** Usually O(log n) levels with O(n) work each = O(n log n)
- **Master Theorem:** For recurrences of form T(n) = aT(n/b) + f(n)

### 4. Drop Constants and Lower Order Terms
- O(2n) becomes O(n)
- O(n² + n) becomes O(n²)
- O(100) becomes O(1)

### Examples

**Example 1: Simple Loop**
```
for i from 0 to n-1:
    print(i)
```
- Loop runs n times
- Time Complexity: **O(n)**

**Example 2: Nested Loops**
```
for i from 0 to n-1:
    for j from 0 to n-1:
        print(i, j)
```
- Outer loop: n iterations
- Inner loop: n iterations per outer iteration
- Total: n × n = n²
- Time Complexity: **O(n²)**

**Example 3: Logarithmic**
```
i = 1
while i < n:
    i = i * 2
```
- i doubles each iteration: 1, 2, 4, 8, ..., n
- Number of iterations: log₂(n)
- Time Complexity: **O(log n)**

**Example 4: Mixed**
```
for i from 0 to n-1:
    for j from 0 to i:
        print(i, j)
```
- Inner loop runs: 1 + 2 + 3 + ... + n = n(n+1)/2
- Time Complexity: **O(n²)**

---

## Space Complexity

Space complexity measures the total memory used by an algorithm, excluding the input itself.

### Components
1. **Fixed Part:** Instructions, constants, variables
2. **Variable Part:** Recursion stack, dynamically allocated memory

### Examples

**Example 1: Constant Space**
```
sum = 0
for i from 0 to n-1:
    sum = sum + array[i]
```
- Only uses sum and i variables
- Space Complexity: **O(1)**

**Example 2: Linear Space**
```
function factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)
```
- Recursion stack depth: n
- Space Complexity: **O(n)**

**Example 3: Linear Space (Array)**
```
function copy_array(arr):
    new_arr = new array of size n
    for i from 0 to n-1:
        new_arr[i] = arr[i]
    return new_arr
```
- New array of size n
- Space Complexity: **O(n)**

---

## Best, Average, and Worst Case

### Best Case
The minimum time/space required for any input of size n.
- Example: Finding element at first position in linear search: **O(1)**

### Average Case
The expected time/space for a typical random input.
- Example: Average position in linear search: **O(n/2)** = **O(n)**

### Worst Case
The maximum time/space required for any input of size n.
- Example: Element at end or not present in linear search: **O(n)**

### Why Focus on Worst Case?
1. Provides performance guarantees
2. Easier to analyze mathematically
3. Most important for critical systems
4. Best case is often not realistic

---

## Amortized Analysis

Some operations are expensive but occur rarely. Amortized analysis gives the average performance over a sequence of operations.

### Example: Dynamic Array
- Most appends: O(1)
- Resize append: O(n) but happens only every n operations
- **Amortized:** O(1) per operation

### Methods
1. **Aggregate Method:** Total cost / number of operations
2. **Accounting Method:** Assign different costs to operations
3. **Potential Method:** Use potential function to track "prepaid" work

---

## Common Patterns

### O(1) - Constant Time
- Array access by index
- Hash table operations (average case)
- Stack/Queue push/pop

### O(log n) - Logarithmic
- Binary search
- Balanced BST operations
- Divide and conquer steps

### O(n) - Linear
- Single loop through array
- Linear search
- Finding max/min in unsorted array

### O(n log n) - Linearithmic
- Efficient sorting algorithms
- Divide and conquer algorithms
- Merge sort, quicksort, heapsort

### O(n²) - Quadratic
- Bubble sort, selection sort, insertion sort
- Nested loops comparing all pairs
- Simple matrix operations

### O(2ⁿ) - Exponential
- Generating all subsets
- Recursive Fibonacci (naive)
- Brute force solutions

---

## Tips for Analysis

1. **Focus on dominant terms:** n² + n is O(n²)
2. **Worst case assumptions:** Assume unfavorable input patterns
3. **Consider space for recursion:** Each recursive call uses stack space
4. **Look for early termination:** Some algorithms may stop early (best case)
5. **Consider data structure operations:** Array vs linked list have different complexities
6. **Amortized vs worst-case:** Dynamic arrays, hash table resizing

---

## Space-Time Tradeoffs

Often, you can trade space for time:

- **Memoization:** Store results to avoid recomputation (more space, less time)
- **Preprocessing:** Sort data first to enable binary search (more space/time initially, faster queries)
- **Hash Tables:** O(1) lookup at cost of O(n) space

Choose based on your constraints:
- Limited memory → optimize space
- Real-time requirements → optimize time
- Both constrained → find balance
