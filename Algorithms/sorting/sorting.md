# Sorting Algorithms – Complexity Analysis

---

## 1. Heap Sort – Complexity Analysis

### Building the Max-Heap
- Heapify is applied to `n/2` nodes.
- Each `heapify` takes `O(log n)`.
- Tight bound for building heap: `O(n)`.

### Extracting Elements
- `n` extractions.
- Each extraction calls `heapify` → `O(log n)`.
- Total: `O(n log n)`.

### Time Complexity
- **Best:** `O(n log n)`
- **Average:** `O(n log n)`
- **Worst:** `O(n log n)`

### Space Complexity
- In-place: **O(1)**

### Stability
- **Not stable**

---

## 2. Quick Sort – General Complexity Analysis

### Partitioning
- Partitioning costs `O(n)` per level.

### Time Complexity
- **Best:** `O(n log n)`  
  (balanced partitions)
- **Average:** `O(n log n)`
- **Worst:** `O(n²)`  
  (highly unbalanced partitions)

### Space Complexity
- **Average:** `O(log n)` recursion depth  
- **Worst:** `O(n)` when recursion degenerates

### Stability
- **Not stable**

---

## 3. Quick Sort (Given Code Version)

### Pivot Choice
- Uses **last element** as pivot (`pivot = arr[high]`).
- Performance depends on input order.

### Time Complexity
- **Best:** `O(n log n)`
- **Average:** `O(n log n)`
- **Worst:** `O(n²)`  
  Occurs when:
  - array is already sorted (ascending),
  - reverse sorted,
  - all values identical.

### Space Complexity
- **Average:** `O(log n)`
- **Worst:** `O(n)` (deep recursion)

### Stability
- **Not stable**

### Notes
- Uses Lomuto partition scheme.
- Fully in-place (no extra arrays).
- Simple but pivot selection can be improved (e.g., random pivot, median-of-three).


