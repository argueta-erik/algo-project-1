import time     # import time module to measure duration functions
import random   # import random module to genarate random input data for the algorithms

# ===============
# Time Function
# ===============
def time_function(fn, arr, target=None):

    if (target == None):
        start = time.perf_counter()
        fn(arr)
        end = time.perf_counter()
    else:
        start = time.perf_counter()
        fn(arr, target)
        end = time.perf_counter()

    return (end - start)

# ============
# Bubble Sort
# ============
def bubble_sort(arr):
    n = len(arr)
    # n-1 to fit within the size of the array due to indices
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # swapping the value of the index
    return arr

# ============
# Merge Sort
# ============
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2     # Divide and Conquer
    left = merge_sort(arr[:mid])    # array from left to the midpoint
    right = merge_sort(arr[mid:])   # array from right to the midpoint

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    # comparing both halves and merge
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else: 
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ============
# Quick Sort
# ============
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        LT = []
        EQ = []
        GT = []

        for _ in arr:
            if _ < pivot:
                LT.append(_)
            elif _ == pivot:
                EQ.append(_)
            else:
                GT.append(_)
        return quick_sort(LT) + EQ + quick_sort(GT)

# ============
# Radix Sort
# ============
def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort_radix(arr, exp)
        exp *= 10
    return arr

# counting_sort_radix
def counting_sort_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10    # hard coding the index values

    for i in range(n):
        digit = (arr[i] // exp) % 10
        count[digit] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    i = n - 1
    while i >= 0:
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

# ==============
# Linear Search
# ==============
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1


# =======
# Driver
# =======
def perform_bubble_sort(arr):
    # Bubble Sort
    print("Bubble Sort Algorithm")
    print("Unsorted Array: ", arr)
    time_bubble = time_function(bubble_sort, arr)
    sorted_bubble = bubble_sort(arr)
    print(f"Sorted Array: {sorted_bubble}")
    print(f"Time Elapsed: {time_bubble: .8f} seconds.")


def perform_merge_sort(arr):
    # Merge Sort
    print("\n\nMerge Sort Algorithm")
    print("Unsorted Array: ", arr)
    time_merge = time_function(merge_sort, arr)
    sorted_merge = merge_sort(arr)
    print(f"Sorted Array: {sorted_merge}")
    print(f"Time Elapsed: {time_merge: .8f} seconds.")


def perform_quick_sort(arr):
    print("\n\nQuick Sort Algorithm")
    print("Unsorted Array: ", arr)
    time_quick = time_function(quick_sort, arr)
    sorted_quick = quick_sort(arr)
    print(f"Sorted Array: {sorted_quick}")
    print(f"Time Elapsed: {time_quick: .8f} seconds.")



def perform_radix_sort(arr):
    # Radix Sort
    print("\n\nRadix Sort Algorithm")
    print("Unsorted Array: ", arr)
    time_radix = time_function(radix_sort, arr)
    sorted_radix = radix_sort(arr)
    print(f"Sorted Array: {sorted_radix}")
    print(f"Time Elapsed: {time_radix: .8f} seconds.")


def perform_linear_search(arr):
    # Linear Search
    print("\n\nLinear Search Algorithm")
    print("Given Array: ", arr)
    target = int(input("Please enter a number from the array: \n> "))
    start = time.perf_counter()
    index = linear_search(arr, target)
    end = time.perf_counter()
    time_linear = end - start
    print(f"{target} was located at index: {index}.")
    print(f"Time Elapsed: {time_linear: .8f} seconds.")


# main
if __name__ == "__main__":
    test_arr = [64, 34, 25, 12, 22, 11, 90, 5, 22, 11]

    perform_bubble_sort(test_arr.copy())
    perform_merge_sort(test_arr.copy())
    perform_quick_sort(test_arr.copy())
    perform_radix_sort(test_arr.copy())
    perform_linear_search(test_arr.copy())    # Linear Search is not outputting the index!

    