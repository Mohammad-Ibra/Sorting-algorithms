# SORTING ALGORITHMS

**Definition:**

A Sorting Algorithm is used to rearrange a given array or list elements according to a comparison operator on the elements. The comparison operator is used to decide the new order of elements in the respective data structure.

**Examples of sorting algorithms:**

    1. Selection sort
    2. Bubble sort
    3. Insertion sort
    4. Merge sort
    5. Quick sort
    6. Heap sort
    7. Counting sort
    8. Radix sort

### Selection sort Algorithm

The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

- The subarray which is already sorted. 
- Remaining subarray which is unsorted.

In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray. 

**How it works?**

```
1. Initialize minimum value(min_idx) to location 0
2. Traverse the array to find the minimum element in the array
3. While traversing if any element smaller than min_idx is found then swap both the values.
4. Then, increment min_idx to point to next element
5. Repeat until array is sorted
```
