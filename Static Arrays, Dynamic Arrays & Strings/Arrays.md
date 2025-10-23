# Static Arrays, Dynamic Arrays & Strings

## Arrays

* An array is a contiguous block of memory with a fixed size. They have indices starting from 0 to (size - 1).

* An array's index position can be accessed at constant time O(1).

* Arrays are mutable objects (changeable). Even tho the array's size cannot be changed, we can change the values at a particular index. So index updates are also done at constant time O(1).

* **Searching**: Check if a certain value is in the array. This requires iterating through the entire array in the worst case, so it takes linear time O(n).

* **Insertion**: Inserting an element into an array is not possible if the array is full. If there is space (in the end), it can be done in constant time O(1). However, inserting at the beginning or in the middle (when full) requires shifting elements, which takes linear time O(n) and also gets rid of the last element.

* **Deletion**: Deleting an element from an array is not possible if the array is empty. If there are elements to delete, it can be done in constant time O(1) if we are removing the last element as no shifting is required. However, removing an element from the beginning or middle requires shifting elements, which takes linear time O(n).

* Shifting is required because arrays have to be kept as a contiguous block of memory and gaps in the middle are not allowed, but gaps in the end are allowed as they *are* contiguous.

* Static arrays are very limiting, but they are how underlying computer memory actually work. Generally in a programming language, static arrays are wrapped in a more flexible data structure called a **dynamic array**.

* **Dynamic Array**: Is essentially a static array that can change size. How they do this is they dynamically allocate a new static array with a larger size (usually double the current size), copy over all the elements from the old array to the new array, and then free the old array. This resizing operation takes linear time O(n) because of the copying. A dynamic array is made up for several different static arrays over time.

  * If we initialize ```python A = [1,2]``` in python, what actually is created is a static array of size = 4. ```python A = [1,2,x,x]```, where x are empty slots. When we append more elements, the dynamic array will resize itself in orders of 2 as needed.

  * So appending an element to a dynamic array takes **amortized constant time** ***O(1)** because most of the time there is space to add the element, but occasionally it needs to resize which takes linear time O(n). Over many appends, the average time per append is still constant time O(1).

* When ever we mention "list", it is usually a dynamic array.

* **Strings**: Written in quotes (ex: 'abc'), is also a contiguous block of memory, similar to an array of characters. Strings are immutable (unchangeable), so any operation that modifies a string actually creates a new string in memory.

* As they are immutable, any operation that modifies a string (like insertion, deletion, concatenation) takes linear time O(n) because a new string has to be created and the characters copied over and updation is not allowed.

---

### 🧠 Static vs Dynamic Arrays vs Strings – Time Complexity Chart

| Operation                          | **Static Array** | **Dynamic Array (e.g., Python list, C++ vector)** | **String** |
| ---------------------------------- | ---------------- | ------------------------------------------------- | ---------- |
| **Access (by index)**              | O(1)             | O(1)                                              | O(1)       |
| **Search (unsorted)**              | O(n)             | O(n)                                              | O(n)       |
| **Search (sorted, binary search)** | O(log n)         | O(log n)                                          | O(log n)   |
| **Insert at end (amortized)**      | N/A (fixed size) | O(1)*                                             | O(n)       |
| **Insert at end (worst case)**     | N/A              | O(n) (when resizing)                              | O(n)       |
| **Insert at beginning / middle**   | O(n)             | O(n)                                              | O(n)       |
| **Delete at end**                  | N/A              | O(1)                                              | O(n)       |
| **Delete at beginning / middle**   | O(n)             | O(n)                                              | O(n)       |
| **Resize / Reallocate**            | N/A              | O(n) (copying elements)                           | O(n)       |
| **Copy / Clone**                   | O(n)             | O(n)                                              | O(n)       |
| **Concatenation (`A + B`)**        | N/A              | O(n + m)                                          | O(n + m)   |
| **Space Complexity**               | O(n)             | O(n) (may allocate extra)                         | O(n)       |

*Amortized time means that while a single operation might take longer, when averaged over a sequence of operations, the average time per operation is constant.*

---
