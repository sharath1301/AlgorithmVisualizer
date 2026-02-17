# Tree and Graph Algorithms

Trees and graphs are fundamental data structures for organizing hierarchical and networked data. Understanding traversal and manipulation algorithms is essential for working with complex data relationships.

---

## Binary Search Tree (BST) Operations

### Overview
A binary tree where for each node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater.

### Time Complexity
- **Search, Insert, Delete:**
  - Average: O(log n) for balanced trees
  - Worst: O(n) for skewed trees

---

#### BST Search

##### Algorithm Steps
1. Start at the root node
2. Compare target value with current node's value
3. If equal, return the node (found)
4. If target < current value, move to left child
5. If target > current value, move to right child
6. Repeat steps 2-5 until found or reach null (not found)

##### Visualization States
- **Current Node:** Node being examined
- **Comparing:** Checking against target
- **Going Left:** Target is smaller
- **Going Right:** Target is larger
- **Found/Not Found:** Search result

---

#### BST Insertion

##### Algorithm Steps
1. Start at the root node
2. If tree is empty, create new node as root
3. Compare new value with current node
4. If new value < current:
   a. If left child is null, insert as left child
   b. Otherwise, move to left child and repeat
5. If new value > current:
   a. If right child is null, insert as right child
   b. Otherwise, move to right child and repeat
6. If value exists (optional), handle according to policy (ignore/update)

##### Visualization States
- **Traversing:** Finding insertion point
- **Comparing:** Deciding left or right
- **Inserting:** Adding new node

---

#### BST Deletion

##### Algorithm Steps
1. Find the node to delete using search
2. Case 1: Node is a leaf (no children)
   - Simply remove the node
3. Case 2: Node has one child
   - Replace node with its child
4. Case 3: Node has two children
   a. Find inorder successor (smallest in right subtree) or predecessor (largest in left subtree)
   b. Copy successor's value to the node
   c. Recursively delete the successor

##### Visualization States
- **Finding:** Locating target node
- **Identifying Case:** Determining number of children
- **Finding Successor:** Searching for replacement
- **Replacing:** Swapping values
- **Removing:** Deleting node

---

## Tree Traversals

### Inorder Traversal (Left-Root-Right)

#### Algorithm Steps
1. Recursively traverse the left subtree
2. Visit/Process the root node
3. Recursively traverse the right subtree

#### Output
For BST, produces values in ascending sorted order.

---

### Preorder Traversal (Root-Left-Right)

#### Algorithm Steps
1. Visit/Process the root node
2. Recursively traverse the left subtree
3. Recursively traverse the right subtree

#### Use Cases
- Creating a copy of the tree
- Serializing the tree
- Prefix expression evaluation

---

### Postorder Traversal (Left-Right-Root)

#### Algorithm Steps
1. Recursively traverse the left subtree
2. Recursively traverse the right subtree
3. Visit/Process the root node

#### Use Cases
- Deleting a tree (delete children before parent)
- Postfix expression evaluation
- Calculating directory sizes

---

### Level Order Traversal (BFS)

#### Algorithm Steps
1. Create a queue and enqueue the root
2. While queue is not empty:
   a. Dequeue a node and process it
   b. Enqueue its left child if exists
   c. Enqueue its right child if exists

#### Use Cases
- Finding the height of tree
- Finding the deepest node
- Breadth-first exploration

---

## Heap Operations

### Overview
A complete binary tree where parent nodes follow a specific ordering property:
- **Max-Heap:** Parent ≥ Children
- **Min-Heap:** Parent ≤ Children

### Time Complexity
- **Insert:** O(log n)
- **Extract Max/Min:** O(log n)
- **Build Heap:** O(n)
- **Peek (Get Max/Min):** O(1)

---

#### Heap Insert

##### Algorithm Steps (Max-Heap)
1. Add new element at the next available position (maintain complete tree)
2. Compare with its parent
3. If new element > parent, swap them
4. Continue comparing and swapping up the tree until heap property is restored
5. This process is called "bubble up" or "sift up"

##### Visualization States
- **Adding:** Placing at end
- **Comparing with Parent:** Checking heap property
- **Swapping:** Moving up the tree
- **Restored:** Heap property satisfied

---

#### Heap Extract Max

##### Algorithm Steps (Max-Heap)
1. Store the root (maximum) value
2. Move the last element to the root position
3. Remove the last element
4. Compare new root with its children
5. If root < larger child, swap with that child
6. Continue comparing and swapping down until heap property is restored
7. This process is called "bubble down" or "sift down"
8. Return the stored maximum value

##### Visualization States
- **Saving Max:** Storing root value
- **Moving Last:** Bringing last element to root
- **Sifting Down:** Restoring heap property
- **Returning:** Outputting max value

---

#### Build Heap

##### Algorithm Steps (Max-Heap)
1. Start with the last non-leaf node: index = n/2 - 1
2. Apply sift down operation on this node
3. Move to the previous node (index--)
4. Repeat sift down for all non-leaf nodes going up to the root
5. This bottom-up approach is more efficient than inserting elements one by one

---

## Graph Traversals

### Depth-First Search (DFS) for Graphs

#### Algorithm Steps
1. Choose a starting vertex, mark it as visited
2. Explore an unvisited adjacent vertex recursively
3. When no unvisited adjacent vertices remain, backtrack
4. Continue until all reachable vertices are visited
5. If disconnected components exist, repeat from unvisited vertex

#### Implementation Options
- **Recursive:** Uses call stack
- **Iterative:** Explicit stack data structure

#### Visualization States
- **Visiting:** Current vertex
- **Exploring:** Checking neighbors
- **Backtracking:** Return to previous vertex
- **Completed:** All reachable vertices visited

---

### Breadth-First Search (BFS) for Graphs

#### Algorithm Steps
1. Choose a starting vertex, mark it as visited, enqueue it
2. While queue is not empty:
   a. Dequeue a vertex
   b. Visit/process the vertex
   c. Enqueue all unvisited adjacent vertices
   d. Mark them as visited
3. If disconnected components exist, repeat from unvisited vertex

#### Visualization States
- **Queue:** Vertices waiting to be processed
- **Processing:** Current vertex
- **Enqueueing:** Adding neighbors
- **Level:** Distance from start

---

### Applications of Graph Traversals

#### Cycle Detection (DFS)
- Keep track of the recursion stack
- If we encounter a vertex that's in the current recursion stack, a cycle exists

#### Topological Sort
- For Directed Acyclic Graphs (DAGs)
- Ordering where every edge goes from earlier to later in the order
- Use DFS: add vertex to result after exploring all descendants (reverse postorder)

#### Connected Components
- Use DFS or BFS to find all vertices reachable from a starting vertex
- Repeat from unvisited vertices to find all components

#### Shortest Path (unweighted)
- BFS naturally finds shortest path in unweighted graphs
- Track parent pointers to reconstruct path

---

## Advanced Tree Operations

### Tree Height/Depth

#### Algorithm Steps
1. If node is null, return -1 (or 0 for single node = height 0)
2. Recursively calculate height of left subtree
3. Recursively calculate height of right subtree
4. Return 1 + maximum of left and right heights

---

### Tree Balancing (AVL/Red-Black Trees)

#### Balance Factor (AVL)
- Balance Factor = Height(Left) - Height(Right)
- Must be -1, 0, or +1 for balanced node

#### Rotations
1. **Left Rotation:** When right subtree is too heavy
2. **Right Rotation:** When left subtree is too heavy
3. **Left-Right Rotation:** Left rotation on left child, then right rotation
4. **Right-Left Rotation:** Right rotation on right child, then left rotation

---

### Lowest Common Ancestor (LCA)

#### Algorithm Steps
1. If current node is null, return null
2. If current node equals either target, return current
3. Recursively search in left and right subtrees
4. If both left and right return non-null, current is LCA
5. Otherwise, return the non-null result (or null if both null)

---

## Comparison Summary

| Operation | Array | BST (avg) | BST (worst) | Heap |
|-----------|-------|-----------|-------------|------|
| Search | O(n) | O(log n) | O(n) | O(n) |
| Insert | O(1)* | O(log n) | O(n) | O(log n) |
| Delete | O(n) | O(log n) | O(n) | O(log n) |
| Min/Max | O(n) | O(log n)** | O(n) | O(1) |

*at end, **requires tree traversal to find
