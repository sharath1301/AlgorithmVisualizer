# Sorting Algorithms

Sorting algorithms arrange elements in a specific order (typically ascending or descending). Understanding these algorithms helps build intuition about algorithmic thinking, time/space complexity, and optimization techniques.

---

## Bubble Sort

### Overview
A simple comparison-based algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

### Time Complexity
- **Best Case:** O(n) when array is already sorted
- **Average Case:** O(n²)
- **Worst Case:** O(n²)
- **Space Complexity:** O(1)

### Algorithm Steps
1. Start with the first element and compare it with the next element
2. If the current element is greater than the next element, swap them
3. Move to the next pair of elements and repeat step 2
4. Continue this process until you reach the end of the array
5. After one complete pass, the largest element will have "bubbled up" to the end
6. Repeat the process for the remaining elements (excluding the already sorted portion at the end)
7. Continue until no swaps are needed in a complete pass

### Visualization States
- **Comparing:** Two adjacent elements being compared
- **Swapping:** Elements being exchanged
- **Sorted:** Elements in their final position
- **Unsorted:** Elements yet to be processed

### Key Insight
The optimization of checking if any swaps occurred in a pass allows the algorithm to terminate early if the array becomes sorted before completing all passes.

---

## Selection Sort

### Overview
Divides the array into a sorted and unsorted region. Repeatedly selects the minimum element from the unsorted region and places it at the end of the sorted region.

### Time Complexity
- **Best Case:** O(n²)
- **Average Case:** O(n²)
- **Worst Case:** O(n²)
- **Space Complexity:** O(1)

### Algorithm Steps
1. Start with the first position as the minimum
2. Scan the entire unsorted portion to find the actual minimum element
3. Swap the found minimum with the element at the current position
4. Expand the sorted boundary by one position
5. Repeat steps 2-4 for all remaining positions

### Visualization States
- **Current Minimum:** Element currently considered as minimum
- **Scanning:** Comparing elements to find the true minimum
- **Swapping:** Moving the minimum to its correct position
- **Sorted:** Fixed elements in final position

### Key Insight
Selection sort makes exactly n-1 swaps, making it efficient when write operations are expensive (though comparisons remain O(n²)).

---

## Insertion Sort

### Overview
Builds the sorted array one element at a time by repeatedly taking the next element and inserting it into the correct position within the already sorted portion.

### Time Complexity
- **Best Case:** O(n) when array is already sorted
- **Average Case:** O(n²)
- **Worst Case:** O(n²)
- **Space Complexity:** O(1)

### Algorithm Steps
1. Consider the first element as a sorted subarray of size 1
2. Take the next element from the unsorted portion
3. Compare it with elements in the sorted portion from right to left
4. Shift all larger elements one position to the right
5. Insert the element in the correct position
6. Repeat steps 2-5 until all elements are processed

### Visualization States
- **Key Element:** Element being inserted
- **Comparing:** Comparing key with sorted portion
- **Shifting:** Moving larger elements right
- **Inserted:** Element placed in correct position

### Key Insight
Insertion sort is efficient for small datasets and nearly sorted arrays. It performs well in practice for partially sorted data.

---

## Merge Sort

### Overview
A divide-and-conquer algorithm that divides the array into halves, recursively sorts them, and then merges the sorted halves.

### Time Complexity
- **Best Case:** O(n log n)
- **Average Case:** O(n log n)
- **Worst Case:** O(n log n)
- **Space Complexity:** O(n)

### Algorithm Steps

#### Divide Phase:
1. Find the middle point of the array
2. Divide the array into two halves
3. Recursively apply merge sort to the left half
4. Recursively apply merge sort to the right half

#### Merge Phase:
5. Create temporary arrays for both halves
6. Compare elements from both temporary arrays
7. Place the smaller element into the original array
8. Move the pointer of the array from which the element was taken
9. Copy any remaining elements from the non-empty temporary array
10. Repeat until all elements are merged back

### Visualization States
- **Dividing:** Splitting the array recursively
- **Merging:** Combining two sorted subarrays
- **Comparing:** Choosing between left and right elements
- **Placing:** Putting element in final position

### Key Insight
Merge sort's consistent O(n log n) performance makes it reliable for large datasets, though it requires additional space proportional to the input size.

---

## Quick Sort

### Overview
Another divide-and-conquer algorithm that picks a 'pivot' element and partitions the array around it, such that elements smaller than the pivot are on the left and larger elements are on the right.

### Time Complexity
- **Best Case:** O(n log n)
- **Average Case:** O(n log n)
- **Worst Case:** O(n²) - occurs with poor pivot choices
- **Space Complexity:** O(log n) for recursion stack

### Algorithm Steps
1. Choose a pivot element from the array (can be first, last, middle, or random)
2. Initialize pointers at the start and end of the array
3. Move the left pointer right until finding an element ≥ pivot
4. Move the right pointer left until finding an element ≤ pivot
5. If pointers haven't crossed, swap the elements at these pointers
6. Continue steps 3-5 until pointers cross
7. Place the pivot in its final sorted position
8. Recursively apply quick sort to the left subarray
9. Recursively apply quick sort to the right subarray

### Visualization States
- **Pivot Selection:** Choosing the pivot element
- **Partitioning:** Organizing elements around pivot
- **Pointer Movement:** Left and right pointer positions
- **Swapping:** Exchanging out-of-place elements
- **Pivot Placement:** Final position of pivot

### Key Insight
The choice of pivot significantly affects performance. Random pivot or median-of-three strategy helps avoid worst-case scenarios.

---

## Heap Sort

### Overview
Uses a binary heap data structure to sort elements. Builds a max-heap and repeatedly extracts the maximum element.

### Time Complexity
- **Best Case:** O(n log n)
- **Average Case:** O(n log n)
- **Worst Case:** O(n log n)
- **Space Complexity:** O(1)

### Algorithm Steps

#### Build Max-Heap:
1. Start from the last non-leaf node
2. Apply heapify operation (sift down) to maintain heap property
3. Move to the previous node and repeat
4. Continue until reaching the root

#### Sort Phase:
5. Swap the root (maximum element) with the last element
6. Reduce heap size by 1
7. Heapify the root to maintain heap property
8. Repeat steps 5-7 until heap size is 1

#### Heapify Operation:
- Compare parent with left and right children
- If parent is smaller than either child, swap with the larger child
- Continue down the tree until heap property is restored

### Visualization States
- **Building Heap:** Creating the initial max-heap
- **Heapifying:** Maintaining heap property after removal
- **Extracting Max:** Moving maximum to sorted portion
- **Heap Structure:** Visualizing the tree structure

### Key Insight
Heap sort has guaranteed O(n log n) performance and uses O(1) extra space, making it suitable for memory-constrained environments.

---

## Comparison Table

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |

---

## When to Use Each Algorithm

- **Bubble Sort:** Educational purposes only; rarely used in practice
- **Selection Sort:** When memory writes are expensive
- **Insertion Sort:** Small datasets or nearly sorted data
- **Merge Sort:** Stable sort needed, external sorting (large files)
- **Quick Sort:** General purpose, cache-friendly, fastest on average
- **Heap Sort:** Memory-constrained environments, guaranteed O(n log n)
