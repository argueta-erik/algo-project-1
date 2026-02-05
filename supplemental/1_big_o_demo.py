# ================================================================
# BIG O COMPLEXITY: REAL IMPACT DEMONSTRATION
# ================================================================
# This script shows how different Big O time complexities behave
# in practice by timing real Python functions on growing inputs. [web:18]
# You can run it directly in IDLE (F5) or from the command line.
# ================================================================

# Import the time module so we can measure how long functions take. [web:18]
import time

# Import random so we can generate random input data for sorting demos. [web:19]
import random


# ================================================================
# PART 1: SEARCH ALGORITHMS - O(1) vs O(n) vs O(log n)
# ================================================================

def get_first_element(arr):
    # Define a function that returns the first element of a list.
    # This is an O(1) operation because it does a single index lookup
    # regardless of how large the list is. [web:19]
    return arr[0]


def linear_search(arr, target):
    # Define a function that searches for a target in a list linearly.
    # This is O(n) because in the worst case it checks every element once. [web:18]
    for x in arr:
        # Loop over each element in the list.
        if x == target:
            # If the current element equals the target, return True.
            return True
    # If we finish the loop with no match, the target is not in the list.
    return False


def binary_search(arr, target):
    # Define a binary search function that works on a sorted list.
    # This is O(log n) because it halves the search space each step. [web:18]
    left = 0                 # Start of the search range (left index).
    right = len(arr) - 1     # End of the search range (right index).

    # Continue while the search range is valid (left has not passed right).
    while left <= right:
        mid = (left + right) // 2   # Compute middle index of current range.
        if arr[mid] == target:
            # If middle element is the target, we found it.
            return True
        elif arr[mid] < target:
            # If middle value is less than target, move left bound rightward.
            left = mid + 1
        else:
            # If middle value is greater, move right bound leftward.
            right = mid - 1

    # If the loop ends, target is not present in the list.
    return False


def time_search_function(fn, arr, target=None, repeats=3):
    # Helper function to time search-like functions.
    # It supports functions that take one parameter (arr) and
    # functions that take two parameters (arr, target). [web:18]

    start = time.perf_counter()
    # Record the starting high-precision time.

    for _ in range(repeats):
        # Repeat the timing several times to smooth out noise. [web:18]
        if target is None:
            # If no target is provided, call function with only the array.
            fn(arr)
        else:
            # If target is provided, call function with array and target.
            fn(arr, target)

    end = time.perf_counter()
    # Record the ending time after all repeats.

    avg_time = (end - start) / repeats
    # Compute average time per call by dividing total time by repeats.

    return avg_time
    # Return the average time so caller can print or compare it.


def demonstrate_search_algorithms():
    # Run the search demo for different input sizes and print timings.
    print("\n" + "=" * 70)
    # Print a visual separator line to make output easier to read.
    print("PART 1: SEARCH ALGORITHMS - O(1) vs O(n) vs O(log n)")
    # Label this section of the demo for the user.
    print("=" * 70)

    test_sizes = [10_000, 100_000, 1_000_000]
    # Define the list sizes n we want to test (10K, 100K, 1M). [web:18]

    for n in test_sizes:
        # Loop over each test input size.
        arr = list(range(n))
        # Create a sorted list [0, 1, 2, ..., n-1] to use in searches. [web:18]

        target = -1
        # Choose a target that is not in the list to force worst-case linear search.

        print(f"\n{'-' * 70}")
        # Print a subsection separator for each n.
        print(f"Array size: n = {n:,} elements")
        # Show the current array size with commas for readability.

        t_first = time_search_function(get_first_element, arr, repeats=5)
        # Time O(1) access: get_first_element just reads arr[0]. [web:19]
        print(f"  O(1) get_first_element:      {t_first:.8f} seconds")
        # Print average O(1) time with high precision.

        t_linear = time_search_function(linear_search, arr, target, repeats=3)
        # Time O(n) linear search using arr and target. [web:18]
        print(f"  O(n) linear_search:          {t_linear:.6f} seconds")
        # Print average O(n) time with microsecond-level precision.

        t_binary = time_search_function(binary_search, arr, target, repeats=5)
        # Time O(log n) binary search on sorted arr. [web:18]
        print(f"  O(log n) binary_search:      {t_binary:.8f} seconds")
        # Print average O(log n) time with high precision.

        if t_binary > 0:
            # Avoid division by zero when computing speedup.
            speedup = t_linear / t_binary
            # Compute how many times faster binary search is versus linear search.
            print(f"\n  ➤ Speedup: binary is about {speedup:.1f}x faster than linear")
            # Display the speedup factor to highlight impact of complexity.


# ================================================================
# PART 2: SORTING ALGORITHMS - O(n²) vs O(n log n)
# ================================================================

def selection_sort(arr):
    # Implement selection sort, a simple O(n²) sorting algorithm. [web:20]
    a = arr[:]                # Make a shallow copy so we do not modify original.
    n = len(a)                # Get number of elements to know the loop bounds.

    for i in range(n):
        # Outer loop chooses index where next smallest element will go.
        min_idx = i
        # Assume current position i holds minimum value initially.

        for j in range(i + 1, n):
            # Inner loop scans the unsorted tail for a smaller element.
            if a[j] < a[min_idx]:
                # If we find a smaller element, remember its index.
                min_idx = j

        a[i], a[min_idx] = a[min_idx], a[i]
        # Swap the smallest element found into correct position i. [web:20]

    return a
    # Return the sorted copy.


def time_sort_function(fn, data, repeats=3):
    # Time a sorting function that takes a list and returns a sorted list.
    start = time.perf_counter()
    # Record the starting time.

    for _ in range(repeats):
        # Repeat sorting to smooth out timing noise.
        fn(data)
        # Call the sorting function on the same input list each time.

    end = time.perf_counter()
    # Record the ending time.

    avg_time = (end - start) / repeats
    # Compute average time per run.

    return avg_time
    # Return average time.


def demonstrate_sort_algorithms():
    # Run the sorting demo comparing O(n²) vs O(n log n). [web:20]
    print("\n" + "=" * 70)
    # Print section separator lines.
    print("PART 2: SORTING ALGORITHMS - O(n²) vs O(n log n)")
    # Label this section clearly.
    print("=" * 70)

    test_sizes = [1_000, 5_000, 10_000]
    # Define list sizes for the sorting demo (kept modest for O(n²)). [web:18]

    for n in test_sizes:
        # Loop over each list size.
        data = [random.randint(0, 1_000_000) for _ in range(n)]
        # Generate n random integers as unsorted input data. [web:19]

        print(f"\n{'-' * 70}")
        # Print subsection separator.
        print(f"Array size: n = {n:,} elements (random unsorted data)")
        # Show current list size and note that data is random.

        t_selection = time_sort_function(selection_sort, data, repeats=1)
        # Time our O(n²) selection_sort; one run is usually enough due to slowness. [web:20]
        print(f"  O(n²) selection_sort:        {t_selection:.6f} seconds")
        # Print time for the quadratic sort.

        t_builtin = time_sort_function(sorted, data, repeats=3)
        # Time Python's built-in sorted, which is O(n log n) in worst case. [web:19]
        print(f"  O(n log n) sorted():         {t_builtin:.6f} seconds")
        # Print time for the efficient sort.

        if t_builtin > 0:
            # Avoid division by zero when computing ratio.
            ratio = t_selection / t_builtin
            # Compute how many times slower selection_sort is versus sorted.
            print(f"\n  ➤ selection_sort is about {ratio:.1f}x slower than sorted()")
            # Show performance penalty of O(n²) vs O(n log n).


# ================================================================
# PART 3: EXPONENTIAL TIME EXAMPLE - O(2^n)
# ================================================================

def fib_naive_exponential(n):
    # Define a naive recursive Fibonacci implementation.
    # This is O(2^n) because each call spawns two new calls. [web:18]
    if n == 0:
        # Base case: Fibonacci(0) is 0.
        return 0
    elif n == 1:
        # Base case: Fibonacci(1) is 1.
        return 1
    else:
        # Recursive case: sum of previous two Fibonacci numbers.
        return fib_naive_exponential(n - 1) + fib_naive_exponential(n - 2)


def demonstrate_exponential_danger():
    # Show how quickly exponential time grows even for small n. [web:18]
    print("\n" + "=" * 70)
    # Print section separator lines.
    print("PART 3: EXPONENTIAL TIME - O(2^n) FIBONACCI EXAMPLE")
    # Label this section.
    print("=" * 70)

    test_values = [10, 15, 20]
    # Choose small n values to avoid extremely long runtimes.

    print("\nNaive recursive Fibonacci fib(n) = fib(n-1) + fib(n-2)")
    # Explain which Fibonacci version is being used.
    print("This implementation has exponential time complexity (O(2^n)).\n")
    # State the Big O clearly for students. [web:18]

    for n in test_values:
        # Loop over chosen n values for demonstration.
        start = time.perf_counter()
        # Record starting time.

        result = fib_naive_exponential(n)
        # Compute Fibonacci number using the naive recursive function.

        end = time.perf_counter()
        # Record ending time.

        elapsed = end - start
        # Compute time taken for this n.

        print(f"  fib({n:2d}) = {result:>6d}  →  Time: {elapsed:.4f} seconds")
        # Print Fibonacci result and time taken in a readable format.

    print("\n  ⚠ Notice how quickly time grows even for small increases in n.")
    # Highlight the rapid time growth characteristic of exponential algorithms.
    print("  ⚠ For n = 30 or 40 this naive version becomes extremely slow.")
    # Warn that larger n will take impractically long. [web:18]
    print("  💡 In practice we would use dynamic programming or iteration")
    # Suggest using more efficient approaches in real code. [web:18]
    print("     to compute Fibonacci in O(n) time instead of O(2^n).\n")
    # Mention the improved linear-time complexity for comparison. [web:18]


# ================================================================
# MAIN FUNCTION TO RUN ALL DEMOS
# ================================================================

def main():
    # Define the main function that orchestrates the entire demonstration.
    print("\n" + "█" * 70)
    # Print a decorative border line using block characters.
    print("█" + " " * 68 + "█")
    # Print an empty line inside the border.
    title = "BIG O COMPLEXITY: REAL IMPACT DEMONSTRATION"
    # Store the title text in a variable for centering.
    print("█" + title.center(68) + "█")
    # Print the centered title between the border characters.
    print("█" + " " * 68 + "█")
    # Print another empty line inside the border.
    print("█" * 70 + "\n")
    # Close the border and add a blank line.

    print("This script demonstrates how different Big O complexities behave")
    # Briefly explain what the script is about. [web:18]
    print("by timing real Python functions on increasing input sizes.\n")
    # Clarify that we use real timings, not just theoretical formulas. [web:18]

    demonstrate_search_algorithms()
    # Run and print the search algorithm timing demo.

    demonstrate_sort_algorithms()
    # Run and print the sorting algorithm timing demo.

    demonstrate_exponential_danger()
    # Run and print the exponential-time Fibonacci demo.

    print("\n" + "=" * 70)
    # Print final separator line.
    print("DEMO COMPLETE - REFLECT ON HOW QUICKLY RUNTIME CAN GROW WITH n")
    # Encourage students to think about growth rates. [web:18]
    print("=" * 70 + "\n")
    # Close with a final line and blank line.


# ================================================================
# SCRIPT ENTRY POINT
# ================================================================

if __name__ == "__main__":
    # This condition ensures main() only runs when this file is executed
    # directly (e.g., via IDLE or python big_o_demo.py), and not when the
    # file is imported as a module from another script. [web:18]
    main()
    # Call the main function to start the Big O demonstrations.
