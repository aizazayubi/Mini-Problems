## Heap Sort – Complexity Analysis

### 1. Building the Max-Heap
- Heapify is called for roughly `n/2` nodes.
- Each `heapify` operation takes `O(log n)` time.
- Loose bound: `O(n log n)`
- Tighter bound: `O(n)` for building the heap.

### 2. Extracting Elements
- We extract the maximum element `n` times.
- Each extraction requires a `heapify` call.
- Each `heapify` takes `O(log n)`.
- Total: `O(n log n)`

### **Overall Time Complexity**
- **Best:** `O(n log n)`
- **Average:** `O(n log n)`
- **Worst:** `O(n log n)`

### **Space Complexity**
- In-place sorting
- **Space:** `O(1)`

### **Stability**
- Heap Sort is **not stable**
