import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Selecting the middle element as the pivot
    lesser = [element for element in arr if element < pivot]
    equal = [element for element in arr if element == pivot]
    greater = [element for element in arr if element > pivot]
    return quicksort(lesser) + equal + quicksort(greater)

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)  # Randomly selecting a pivot
    lesser = [element for element in arr if element < pivot]
    equal = [element for element in arr if element == pivot]
    greater = [element for element in arr if element > pivot]
    return randomized_quicksort(lesser) + equal + randomized_quicksort(greater)

# Measuring Execution Time
import time

def calculate_execution_time(sorting_function, arr):
    start_time = time.time()
    sorting_function(arr)
    end_time = time.time()
    return end_time - start_time

# Creating Test Cases
sizes = [100, 1000, 5000, 10000]
data_types = {"random": lambda n: [random.randint(0, 10000) for _ in range(n)],
              "sorted": lambda n: list(range(n)),
              "reverse_sorted": lambda n: list(range(n, 0, -1))}

execution_results = {}
for size in sizes:
    for category, generator in data_types.items():
        sample_data = generator(size)
        time_deterministic = calculate_execution_time(quicksort, sample_data[:])
        time_randomized = calculate_execution_time(randomized_quicksort, sample_data[:])
        execution_results[(size, category)] = (time_deterministic, time_randomized)

# Displaying Results
for (size, category), (time_deterministic, time_randomized) in execution_results.items():
    print(f"Size: {size}, Data Type: {category}, Deterministic Time: {time_deterministic:.6f}s, Randomized Time: {time_randomized:.6f}s")