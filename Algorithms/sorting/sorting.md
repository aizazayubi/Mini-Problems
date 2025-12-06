## Heap Sort – Complexity Analysis

### 1. Building the Max-Heap
- Heapify is applied to `n/2` nodes.
- Each `heapify` operation takes `O(log n)`.
- Loose bound: `O(n log n)`
- Tight bound: `O(n)` for heap construction.

### 2. Extracting Elements
- `n` extractions; each calls `heapify`.
- Each `heapify` takes `O(log n)`.
- Total: `O(n log n)`

### **Overall Time Complexity**
- **Best:** `O(n log n)`
- **Average:** `O(n log n)`
- **Worst:** `O(n log n)`

### **Space Complexity**
- In-place
- **Space:** `O(1)`

### **Stability**
- Not stable


---

## Quick Sort – Complexity Analysis

### 1. Partitioning Process
- Each partition divides the list around a pivot.
- Partitioning itself costs `O(n)`.

### 2. Recurrence
- Depends on pivot selection.

### **Time Complexity**
- **Best:** `O(n log n)`  
  (pivot splits the array evenly)
- **Average:** `O(n log n)`  
  (randomised or good pivot selection)
- **Worst:** `O(n²)`  
  (array already sorted + bad pivot like first/last element)

### **Space Complexity**
- Recursive function calls.
- **Average:** `O(log n)`
- **Worst:** `O(n)` if recursion degenerates.

### **Stability**
- Not stable (swaps may disturb equal elements)
