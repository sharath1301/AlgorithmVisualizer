# Pathfinding Algorithms

Pathfinding algorithms find the shortest or most efficient path between two points in a graph or grid. These are fundamental in GPS navigation, video games, network routing, and robotics.

---

## Breadth-First Search (BFS)

### Overview
Explores all neighbor nodes at the present depth before moving on to nodes at the next depth level. Guarantees the shortest path in unweighted graphs.

### Time Complexity
- **Best Case:** O(V + E)
- **Average Case:** O(V + E)
- **Worst Case:** O(V + E)
- **Space Complexity:** O(V)

### Algorithm Steps
1. Start from the source node, mark it as visited
2. Create a queue and enqueue the source node
3. While the queue is not empty:
   a. Dequeue a node from the front of the queue
   b. If this node is the destination, reconstruct and return the path
   c. For each unvisited neighbor of the current node:
      - Mark it as visited
      - Record its parent (the current node)
      - Enqueue it
4. If queue empties without finding destination, no path exists

### Visualization States
- **Source:** Starting point
- **Destination:** Target point
- **Queue:** Nodes waiting to be explored
- **Visited:** Nodes already processed
- **Frontier:** Currently exploring neighbors
- **Path:** Final shortest path

### Key Insight
BFS explores nodes in order of their distance from the source, guaranteeing the shortest path in unweighted graphs. However, it explores in all directions equally, which may not be efficient.

---

## Depth-First Search (DFS)

### Overview
Explores as far as possible along each branch before backtracking. Does not guarantee the shortest path but uses less memory than BFS.

### Time Complexity
- **Best Case:** O(V + E)
- **Average Case:** O(V + E)
- **Worst Case:** O(V + E)
- **Space Complexity:** O(V) for recursion stack

### Algorithm Steps
1. Start from the source node, mark it as visited
2. If current node is the destination, reconstruct and return the path
3. For each unvisited neighbor of the current node:
   a. Mark it as visited
   b. Record its parent
   c. Recursively explore from this neighbor
   d. If path found, return it
   e. Backtrack (unmark if needed for other paths)
4. If all neighbors explored without finding destination, backtrack

### Visualization States
- **Current Path:** The path being explored
- **Backtracking:** Returning to previous node
- **Visited:** Nodes in current exploration
- **Dead End:** Node with no unvisited neighbors

### Key Insight
DFS can find a path quickly but not necessarily the shortest. It's memory-efficient as it only needs to store the current path, not all frontier nodes.

---

## Dijkstra's Algorithm

### Overview
Finds the shortest path from a source node to all other nodes in a weighted graph with non-negative edge weights.

### Time Complexity
- **Best Case:** O((V + E) log V) with binary heap
- **Average Case:** O((V + E) log V)
- **Worst Case:** O((V + E) log V)
- **Space Complexity:** O(V)

### Algorithm Steps
1. Initialize distances: source = 0, all others = infinity
2. Create a priority queue (min-heap) with all nodes
3. While the priority queue is not empty:
   a. Extract the node with minimum distance (current)
   b. If current is the destination, reconstruct and return the path
   c. For each neighbor of current:
      - Calculate tentative distance = current distance + edge weight
      - If tentative distance < neighbor's current distance:
        * Update neighbor's distance
        * Set neighbor's parent to current
        * Update priority queue
4. If destination never reached, no path exists

### Visualization States
- **Distance Values:** Current best known distance to each node
- **Priority Queue:** Nodes ordered by current best distance
- **Settled:** Node with final shortest distance confirmed
- **Relaxing:** Updating neighbor distances
- **Path Reconstruction:** Tracing back from destination

### Key Insight
Dijkstra's algorithm always expands the closest unexplored node, ensuring optimality. The priority queue makes it efficient for sparse graphs.

---

## A* (A-Star) Algorithm

### Overview
An extension of Dijkstra's algorithm that uses a heuristic to guide the search toward the destination, making it much faster in practice.

### Time Complexity
- **Best Case:** O(E)
- **Average Case:** O(E)
- **Worst Case:** O(E) (but much better in practice)
- **Space Complexity:** O(V)

### Algorithm Steps
1. Initialize:
   - g-score (cost from start): source = 0, others = infinity
   - f-score (estimated total cost): all = infinity
2. Add source to open set (priority queue ordered by f-score)
3. While open set is not empty:
   a. Remove node with lowest f-score (current)
   b. If current is destination, reconstruct path
   c. Move current from open to closed set
   d. For each neighbor of current:
      - If neighbor in closed set, skip
      - Calculate tentative g-score = current g-score + edge cost
      - If tentative g-score < neighbor's g-score:
        * Update neighbor's g-score
        * Calculate f-score = g-score + heuristic(neighbor, destination)
        * Set neighbor's parent to current
        * Add neighbor to open set if not already present
4. If open set empties without finding destination, no path exists

### Heuristic Functions
- **Manhattan Distance:** |x1 - x2| + |y1 - y2| (for 4-directional movement)
- **Euclidean Distance:** √((x1-x2)² + (y1-y2)²) (for any-angle movement)
- **Diagonal Distance:** max(|x1-x2|, |y1-y2|) (for 8-directional movement)

### Visualization States
- **Open Set:** Nodes to be evaluated (frontier)
- **Closed Set:** Nodes already evaluated
- **g-score:** Cost from start to current node
- **h-score:** Heuristic estimate to destination
- **f-score:** Total estimated cost (g + h)
- **Path:** Final optimal path

### Key Insight
The heuristic guides the search toward the goal, making A* much faster than Dijkstra for pathfinding. With an admissible heuristic (never overestimates), A* guarantees optimality.

---

## Greedy Best-First Search

### Overview
Always expands the node that appears closest to the goal according to the heuristic, without considering the cost already incurred.

### Time Complexity
- **Best Case:** O(E)
- **Average Case:** O(E)
- **Worst Case:** O(E)
- **Space Complexity:** O(V)

### Algorithm Steps
1. Create a priority queue ordered by heuristic value only
2. Add source node with its heuristic value
3. While queue is not empty:
   a. Remove node with lowest heuristic (current)
   b. If current is destination, return path
   c. For each unvisited neighbor:
      - Calculate heuristic value
      - Add to queue
      - Record parent
4. If queue empties, no path exists

### Key Insight
Very fast but does not guarantee the shortest path. Good when speed is more important than optimality and the heuristic is accurate.

---

## Comparison Table

| Algorithm | Guarantees Shortest Path | Weighted Graphs | Heuristic Needed | Typical Use Case |
|-----------|-------------------------|-----------------|------------------|------------------|
| BFS | Yes (unweighted) | No | No | Unweighted grids, mazes |
| DFS | No | Yes | No | Maze generation, topological sort |
| Dijkstra | Yes | Yes | No | Road networks, network routing |
| A* | Yes (with admissible heuristic) | Yes | Yes | Games, robotics, GPS |
| Greedy Best-First | No | Yes | Yes | Quick approximate solutions |

---

## When to Use Each Algorithm

- **BFS:** Unweighted grids, finding shortest path in terms of steps
- **DFS:** Exploring all paths, topological sorting, detecting cycles
- **Dijkstra:** Weighted graphs where you need guaranteed shortest paths
- **A*:** Interactive applications (games) where both speed and optimality matter
- **Greedy Best-First:** When you need a path quickly and can accept suboptimal results

---

## Grid Movement Variations

### 4-Directional Movement
Can move only up, down, left, right. Use Manhattan distance as heuristic.

### 8-Directional Movement
Can also move diagonally. Use Diagonal distance or Euclidean distance as heuristic. Diagonal moves typically cost √2 or 1.4 times regular moves.

### Weighted Grids
Some cells cost more to traverse (e.g., mud, water). Use Dijkstra or A* with appropriate edge weights.

---

## Obstacles and Special Cells

### Walls/Obstacles
Cells that cannot be traversed. The algorithm must check if a cell is passable before exploring it.

### Swamps/Deserts
Cells with higher movement cost. Weighted algorithms handle these naturally.

### Portals/Teleporters
Special cells that instantly transport to another location. Add edges between portal endpoints.
