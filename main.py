import time
import random

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
    a = arr[:]
    n = len(a)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

# ============
# Merge Sort
# ============
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
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
    if not arr:
        return arr
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort_radix(arr, exp)
        exp *= 10
    return arr

def counting_sort_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

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
def perform_bubble_sort(arr, debug=False):
    print("\nBubble Sort Algorithm")
    time_bubble = time_function(bubble_sort, arr)
    sorted_bubble = bubble_sort(arr)
    
    if debug == True:
        print("Unsorted Array: ", arr)
        print(f"Sorted Array: {sorted_bubble}")

    print(f"Time Elapsed: {time_bubble: .8f} seconds.")
    
    return time_bubble, sorted_bubble

def perform_merge_sort(arr, debug=False):
    print("\n\nMerge Sort Algorithm")
    time_merge = time_function(merge_sort, arr)
    sorted_merge = merge_sort(arr)

    if debug == True:
        print("Unsorted Array: ", arr)
        print(f"Sorted Array: {sorted_merge}")
    
    print(f"Time Elapsed: {time_merge: .8f} seconds.")

    return time_merge, sorted_merge

def perform_quick_sort(arr, debug=False):
    print("\n\nQuick Sort Algorithm")
    time_quick = time_function(quick_sort, arr)
    sorted_quick = quick_sort(arr)
    
    if debug == True:
        print("Unsorted Array: ", arr)    
        print(f"Sorted Array: {sorted_quick}")
    
    print(f"Time Elapsed: {time_quick: .8f} seconds.")

    return time_quick, sorted_quick

def perform_radix_sort(arr, debug=False):
    print("\n\nRadix Sort Algorithm")
    time_radix = time_function(radix_sort, arr)
    sorted_radix = radix_sort(arr)

    if debug == True:
        print("Unsorted Array: ", arr)
        print(f"Sorted Array: {sorted_radix}")

    print(f"Time Elapsed: {time_radix: .8f} seconds.")

    return time_radix, sorted_radix

def perform_linear_search(arr, debug=False):
    print("\n\nLinear Search Algorithm")
    if debug == True:
        print("Given Array: ", arr)
        target = int(input("Please enter a number from the array: \n> "))
    else:
        target = random.choice(arr)

    start = time.perf_counter()
    index = linear_search(arr, target)
    end = time.perf_counter()

    time_linear = end - start

    if index == -1:
        print(f"{target} was not found within the array.")
    else:
        print(f"{target} was located at index: {index}.")
    print(f"Time Elapsed: {time_linear: .8f} seconds.\n")

    return time_linear

def ask_size():
    return int(input(f"Please enter a size for the array.\n> "))

def ask_yn(prompt):
    while True:
            rand_choice = str(input(prompt))
            match rand_choice:
                case 'y':
                    return True
                case 'n':
                    return False
                case 'Y':
                    return True
                case 'N':
                    return False
                case _:
                    print("\nPlease enter a valid option [y/n]")

def set_array(size):
    while True:
        print("Please type number to be entered into the arrray, separated by spaces.")
        print("For example:\n> 1 2 3 4 5 6")
        print("Array: [1, 2, 3, 4, 5, 6]")
        array_input = input("> ")

        temp_arr = list(map(int, array_input.split()))

        if len(temp_arr) == size:
            return temp_arr
        else:
            print(f"\n\nThe array you entered does not match the size: {size}.\nPlease try again.\n\n")

# ==================================
# MAIN FUNCTION TO RUN ALL COMMANDS
# ==================================
def main():
    arr_size = ask_size()
    print_choice = ask_yn("Would you like to see the array(s) printed out? [y/n] \n> ")
    rand_choice = ask_yn("Would you like to use random values? [y/n]\n> ")
    if rand_choice == False:
        user_array = set_array(arr_size)
    else: 
        user_array = [random.choice(range(100)) for _ in range(arr_size)]

    perform_bubble_sort(user_array.copy(), print_choice)
    perform_merge_sort(user_array.copy(), print_choice)
    perform_quick_sort(user_array.copy(), print_choice)
    perform_radix_sort(user_array.copy(), print_choice)
    perform_linear_search(user_array.copy(), print_choice)
    

if __name__ == "__main__":
    main()