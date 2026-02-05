import time     # import time module to measure duration functions
from numpy import random   # import random module to genarate random input data for the algorithms

# ============================================================
# SORTING ALGORITHMS
# ============================================================

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j + 1], arr[j]
    return arr

# ============
# Merge Sort
# ============

# ============
# Quick Sort
# ============

# ============
# Radix Sort
# ============

# ==============
# Linear Search
# ==============


# ===========================================================
# TIME FUNCTION(S)
# ===========================================================

# NOTE TO SELFE: 

# main
if __name__ == "__main__":
    test_arr = [10, 8, 9, 1, 6, 3, 7]
    test_ran_arr = random.randint(10, size=(7))

    print("Unsorted Array:", test_arr)
    print ("Unsorted Random Array:", test_ran_arr)
    print("Bubble Sort:", bubble_sort(test_ran_arr))
