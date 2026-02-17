# Searching Algorithms

Searching algorithms are used to retrieve information stored within a data structure. Understanding different searching techniques helps optimize data retrieval operations.

---

## Linear Search

### Overview
The simplest searching algorithm that checks each element in the collection sequentially until the target is found or the end is reached.

### Time Complexity
- **Best Case:** O(1) - target is the first element
- **Average Case:** O(n)
- **Worst Case:** O(n) - target is last or not present
- **Space Complexity:** O(1)

### Algorithm Steps
1. Start from the first element of the array
2. Compare the current element with the target value
3. If they match, return the current index
4. If they don't match, move to the next element
5. Repeat steps 2-4 until the end of the array
6. If the target is not found after checking all elements, return "not found"

### Visualization States
- **Current Element:** Element being checked
- **Comparing:** Checking if current equals target
- **Found:** Target located at this position
- **Not Found:** Checked all elements, target absent

### Key Insight
Linear search works on both sorted and unsorted arrays and linked lists. It's the only option for unsorted data structures.

---

## Binary Search

### Overview
An efficient algorithm for finding an element in a sorted array by repeatedly dividing the search interval in half.

### Prerequisites
- The array must be sorted
- Random access to elements (arrays, not linked lists)

### Time Complexity
- **Best Case:** O(1) - target is at the middle
- **Average Case:** O(log n)
- **Worst Case:** O(log n)
- **Space Complexity:** O(1) for iterative, O(log n) for recursive

### Algorithm Steps
1. Initialize two pointers: low at the start (0) and high at the end (n-1)
2. While low is less than or equal to high:
   a. Calculate the middle index: mid = low + (high - low) / 2
   b. If the middle element equals the target, return the middle index
   c. If the middle element is greater than the target, set high = mid - 1
   d. If the middle element is less than the target, set low = mid + 1
3. If the loop ends without finding the target, return "not found"

### Visualization States
- **Search Window:** Current range being searched (low to high)
- **Middle Element:** Calculated mid point
- **Comparing:** Checking mid against target
- **Adjusting Range:** Moving low or high pointer
- **Found:** Target located

### Key Insight
Each comparison eliminates half of the remaining elements, making it exponentially faster than linear search for large datasets.

---

## Jump Search

### Overview
A searching algorithm for sorted arrays that works by jumping ahead by fixed steps (block size) and then performing a linear search within the identified block.

### Time Complexity
- **Best Case:** O(1) - target at first jump position
- **Average Case:** O(√n)
- **Worst Case:** O(√n)
- **Space Complexity:** O(1)

### Algorithm Steps
1. Calculate the optimal block size: √n (square root of array size)
2. Jump ahead by block size until finding a block where the target could be
   a. If current element equals target, return index
   b. If current element is greater than target, the target is in the previous block
3. Perform a linear search backward from the current position
4. Check each element in the block until target is found or block boundaries are reached
5. Return the index if found, otherwise "not found"

### Visualization States
- **Jumping:** Moving forward by block size
- **Block Identified:** Found the relevant block
- **Linear Search:** Searching within the block
- **Found/Not Found:** Target status

### Key Insight
Jump search is useful when jumping backward is cheaper than jumping forward (like in linked lists or when caching is involved).

---

## Interpolation Search

### Overview
An improved variant of binary search for uniformly distributed sorted arrays. Instead of always dividing the range in half, it estimates the position of the target based on its value.

### Time Complexity
- **Best Case:** O(1) - target at estimated position
- **Average Case:** O(log log n) for uniformly distributed data
- **Worst Case:** O(n) - for exponentially distributed data
- **Space Complexity:** O(1)

### Algorithm Steps
1. Initialize low and high pointers at array boundaries
2. While low ≤ high and target is within the range [low, high]:
   a. Calculate position using interpolation formula:
      pos = low + [(target - arr[low]) × (high - low)] / (arr[high] - arr[low])
   b. If arr[pos] equals target, return pos
   c. If arr[pos] is less than target, set low = pos + 1
   d. If arr[pos] is greater than target, set high = pos - 1
3. If not found, return "not found"

### Visualization States
- **Estimating Position:** Calculating where target might be
- **Comparing:** Checking estimated position
- **Adjusting Range:** Updating low or high
- **Found:** Target located

### Key Insight
Interpolation search performs exceptionally well on uniformly distributed data (like phone books or dictionaries), but can degrade to linear search on non-uniform distributions.

---

## Exponential Search

### Overview
Also known as doubling search or galloping search, it finds the range where the element exists and then performs binary search within that range.

### Time Complexity
- **Best Case:** O(1) - target at first position
- **Average Case:** O(log n)
- **Worst Case:** O(log n)
- **Space Complexity:** O(1)

### Algorithm Steps
1. Check if the first element is the target
2. Find the range where the element might be present:
   a. Start with index i = 1
   b. While i < n and arr[i] ≤ target, double i (i = i × 2)
3. Perform binary search between indices i/2 and min(i, n-1)
4. Return the result of binary search

### Visualization States
- **Range Finding:** Doubling the search index
- **Binary Search:** Searching within identified range
- **Found/Not Found:** Target status

### Key Insight
Exponential search is particularly useful for unbounded/infinite arrays and when the target is near the beginning of the array.

---

## Comparison Table

| Algorithm | Prerequisites | Best | Average | Worst | Space |
|-----------|--------------|------|---------|-------|-------|
| Linear Search | None | O(1) | O(n) | O(n) | O(1) |
| Binary Search | Sorted, Random Access | O(1) | O(log n) | O(log n) | O(1) |
| Jump Search | Sorted | O(1) | O(√n) | O(√n) | O(1) |
| Interpolation Search | Sorted, Uniform Distribution | O(1) | O(log log n) | O(n) | O(1) |
| Exponential Search | Sorted | O(1) | O(log n) | O(log n) | O(1) |

---

## When to Use Each Algorithm

- **Linear Search:** Unsorted data, linked lists, small datasets
- **Binary Search:** General purpose for sorted arrays, most reliable
- **Jump Search:** When backward jumps are cheaper than forward
- **Interpolation Search:** Uniformly distributed sorted data
- **Exponential Search:** Unbounded arrays, targets near beginning

---

## Binary Search Variations

### Finding First Occurrence
When duplicates exist, modify binary search to continue searching left even after finding a match, to ensure you find the first occurrence.

### Finding Last Occurrence
Similarly, continue searching right after finding a match to locate the last occurrence.

### Finding Insertion Position
When the target doesn't exist, return the position where it should be inserted to maintain sorted order.

### Finding Peak Element
In an array with one peak (first increases, then decreases), use modified binary search to find the peak in O(log n).
