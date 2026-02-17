# Data Structures

Data structures are ways of organizing and storing data to enable efficient access and modification. Choosing the right data structure is crucial for algorithm efficiency.

---

## Arrays

### Overview
A collection of elements stored in contiguous memory locations, accessible by index.

### Characteristics
- **Fixed Size:** Size determined at creation (in many languages)
- **Random Access:** O(1) access by index
- **Cache Friendly:** Elements stored sequentially in memory

### Operations

#### Access by Index
1. Calculate memory address: base_address + (index × element_size)
2. Retrieve value at that address

#### Insert at End
1. Check if array has capacity
2. Store element at next available position
3. Increment size counter

#### Insert at Position
1. Shift all elements from position to end, one position right
2. Store new element at position
3. Increment size

#### Delete from Position
1. Remove element at position
2. Shift all subsequent elements one position left
3. Decrement size

### Time Complexity
- **Access:** O(1)
- **Search:** O(n)
- **Insert at end:** O(1) amortized
- **Insert at position:** O(n)
- **Delete:** O(n)

---

## Linked Lists

### Overview
A linear collection of nodes where each node contains data and a reference to the next node.

### Types
- **Singly Linked:** Each node points to next
- **Doubly Linked:** Each node points to next and previous
- **Circular:** Last node points back to first

### Operations

#### Insert at Beginning
1. Create new node with data
2. Set new node's next to current head
3. Update head to point to new node

#### Insert at End
1. Create new node
2. If list is empty, set as head
3. Otherwise, traverse to last node
4. Set last node's next to new node

#### Delete Node
1. Find the node to delete
2. Update previous node's next to skip current node
3. Free memory (in languages requiring it)

#### Reverse
1. Initialize three pointers: previous = null, current = head, next = null
2. While current is not null:
   a. Store next node
   b. Reverse current's pointer to point to previous
   c. Move previous and current one step forward
3. Update head to previous (new first node)

### Time Complexity
- **Access:** O(n)
- **Search:** O(n)
- **Insert at beginning:** O(1)
- **Insert at end:** O(n) without tail pointer, O(1) with
- **Delete:** O(n)

---

## Stacks

### Overview
A Last-In-First-Out (LIFO) data structure where elements are added and removed from the same end.

### Operations

#### Push (Add)
1. Check for overflow (if fixed size)
2. Increment top pointer
3. Store element at top position

#### Pop (Remove)
1. Check for underflow (empty stack)
2. Retrieve element at top
3. Decrement top pointer
4. Return element

#### Peek (Top)
1. Check for underflow
2. Return element at top without removing

### Applications
- Function call stack
- Expression evaluation
- Backtracking algorithms
- Undo mechanisms

### Time Complexity
- **Push:** O(1)
- **Pop:** O(1)
- **Peek:** O(1)

---

## Queues

### Overview
A First-In-First-Out (FIFO) data structure where elements are added at the rear and removed from the front.

### Types
- **Simple Queue:** Basic FIFO
- **Circular Queue:** Efficient use of fixed array space
- **Priority Queue:** Elements ordered by priority
- **Deque:** Double-ended queue

### Operations

#### Enqueue (Add to rear)
1. Check for overflow
2. Increment rear pointer
3. Store element at rear

#### Dequeue (Remove from front)
1. Check for underflow
2. Retrieve element at front
3. Increment front pointer
4. Return element

#### Circular Queue Optimization
- Use modulo arithmetic: next_position = (current + 1) % capacity
- Reuse space at beginning when elements are dequeued

### Applications
- CPU scheduling
- Print spooling
- Breadth-first search
- Buffering data streams

### Time Complexity
- **Enqueue:** O(1)
- **Dequeue:** O(1)
- **Peek:** O(1)

---

## Hash Tables (Hash Maps)

### Overview
A data structure that maps keys to values using a hash function for fast lookup.

### Components
- **Hash Function:** Converts key to array index
- **Array:** Stores key-value pairs
- **Collision Resolution:** Handles when two keys hash to same index

### Operations

#### Insert
1. Compute hash of key: index = hash(key) % array_size
2. Handle collision if index is occupied
3. Store key-value pair at index

#### Search
1. Compute hash of key
2. Handle collision resolution to find correct slot
3. Return value if key matches

#### Delete
1. Compute hash of key
2. Locate key using collision resolution
3. Mark slot as deleted or remove entry

### Collision Resolution Methods

#### Chaining
- Each array slot contains a linked list
- Colliding keys are added to the list at that index
- Search requires traversing the list

#### Open Addressing
- Find next available slot using probing
- **Linear Probing:** Check next sequential index
- **Quadratic Probing:** Check indices at quadratic intervals
- **Double Hashing:** Use second hash function for step size

### Time Complexity (Average)
- **Insert:** O(1)
- **Search:** O(1)
- **Delete:** O(1)

### Time Complexity (Worst - many collisions)
- **Insert:** O(n)
- **Search:** O(n)
- **Delete:** O(n)

---

## Binary Trees

### Overview
A hierarchical structure where each node has at most two children (left and right).

### Properties
- **Root:** Topmost node
- **Leaf:** Node with no children
- **Height:** Longest path from root to leaf
- **Level:** Distance from root (root = level 0)

### Types
- **Full Binary Tree:** Every node has 0 or 2 children
- **Complete Binary Tree:** All levels filled except possibly last, filled left to right
- **Perfect Binary Tree:** All internal nodes have 2 children, all leaves at same level
- **Balanced Binary Tree:** Height difference between subtrees ≤ 1

### Tree Representations

#### Array Representation (for complete trees)
- Root at index 0
- Left child of node i: 2i + 1
- Right child of node i: 2i + 2
- Parent of node i: (i - 1) / 2

#### Linked Representation
- Each node has data, left pointer, right pointer

---

## Binary Search Trees (BST)

### Overview
Binary tree with ordering property: left subtree < node < right subtree

### Operations Complexity
- **Average:** O(log n) for balanced trees
- **Worst:** O(n) for skewed trees

### Self-Balancing Variants

#### AVL Trees
- Strictly balanced: height difference ≤ 1
- Guarantees O(log n) operations
- More rotations during insert/delete

#### Red-Black Trees
- Loosely balanced
- Less strict than AVL (less rotations)
- Used in many standard libraries (C++ map, Java TreeMap)

---

## Heaps

### Overview
Complete binary tree with heap property (parent ≥ children for max-heap).

### Array Representation
Same formulas as complete binary tree (see above).

### Heap Types
- **Max-Heap:** Parent ≥ Children, root is maximum
- **Min-Heap:** Parent ≤ Children, root is minimum

### Operations
- **Insert:** Add at end, bubble up
- **Extract Max/Min:** Remove root, move last to root, bubble down
- **Build Heap:** Bottom-up heapify

---

## Graphs

### Overview
A collection of vertices (nodes) connected by edges.

### Representations

#### Adjacency Matrix
- 2D array of size V × V
- matrix[i][j] = 1 (or weight) if edge exists from i to j
- Space: O(V²)
- Fast edge lookup: O(1)
- Slow for sparse graphs

#### Adjacency List
- Array of linked lists
- Index represents vertex, list contains neighbors
- Space: O(V + E)
- Fast iteration over neighbors
- Preferred for sparse graphs

#### Edge List
- List of all edges (u, v, weight)
- Space: O(E)
- Simple but slow for neighbor queries

### Graph Types
- **Directed:** Edges have direction
- **Undirected:** Edges bidirectional
- **Weighted:** Edges have associated values
- **Cyclic:** Contains at least one cycle
- **Acyclic:** No cycles (DAG - Directed Acyclic Graph)

---

## Tries (Prefix Trees)

### Overview
A tree-like data structure for storing strings that enables efficient prefix-based searches.

### Structure
- Each node represents a character
- Root represents empty string
- Path from root to node spells a string
- Mark end of word with special flag

### Operations

#### Insert
1. Start at root
2. For each character in word:
   a. If child with that character exists, move to it
   b. Otherwise, create new node and move to it
3. Mark final node as end of word

#### Search
1. Start at root
2. For each character:
   a. If child doesn't exist, word not present
   b. Move to child
3. Return true only if at end of word node

#### Prefix Search
1. Navigate to end of prefix
2. If successful, all descendants form words with that prefix

### Applications
- Autocomplete
- Spell checking
- IP routing (longest prefix match)

### Time Complexity
- **Insert:** O(m) where m = word length
- **Search:** O(m)
- **Prefix Search:** O(m)

---

## Comparison of Data Structures

| Data Structure | Access | Search | Insert | Delete | Space |
|---------------|--------|--------|--------|--------|-------|
| Array | O(1) | O(n) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1)* | O(1)** | O(n) |
| Stack | O(n) | O(n) | O(1) | O(1) | O(n) |
| Queue | O(n) | O(n) | O(1) | O(1) | O(n) |
| Hash Table | - | O(1) | O(1) | O(1) | O(n) |
| BST | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| Heap | O(n) | O(n) | O(log n) | O(log n) | O(n) |

*at beginning, **given pointer to node
