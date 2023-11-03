
import time
import matplotlib.pyplot as plt
import numpy as np

# Naive method for powering a number
def naive_power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

# Divide-and-conquer method for powering a number
def divide_and_conquer_power(base, exponent):
    if exponent == 0:
        return 1
    if exponent % 2 == 0:
        half_power = divide_and_conquer_power(base, exponent // 2)
        return half_power * half_power
    else:
        half_power = divide_and_conquer_power(base, (exponent - 1) // 2)
        return half_power * half_power * base

# Merge Sort algorithm
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Binary Search algorithm
def binary_search(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, r, x)
    else:
        return -1

# Finding all pairs of integers in a set whose sum equals a given number
def find_sum_pairs(arr, sum_value):
    pairs = []
    merge_sort(arr)
    for i in range(len(arr)):
        complement = sum_value - arr[i]
        if binary_search(arr, 0, len(arr) - 1, complement) != -1 and complement != arr[i]:
            pairs.append((arr[i], complement))
    return pairs

# Experimental time measurements
def measure_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time

# Plotting experimental results
def plot_results(exponents, naive_times, divide_conquer_times, sum_pairs_times):
    plt.figure(figsize=(14, 7))
    
    # Plotting powering number results
    plt.subplot(1, 2, 1)
    plt.plot(exponents, naive_times, label='Naive Power')
    plt.plot(exponents, divide_conquer_times, label='Divide and Conquer Power')
    plt.xlabel('Exponent (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Powering Number Time Complexity')
    plt.legend()
    
    # Plotting sum pairs results
    plt.subplot(1, 2, 2)
    plt.plot(exponents, sum_pairs_times, label='Sum Pairs')
    plt.xlabel('Number of Elements (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Sum Pairs Time Complexity')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

# Running the experiments and plotting the results
def run_experiments():
    exponents = [i for i in range(1, 21)]
    naive_times = [measure_time(naive_power, 2, n) for n in exponents]
    divide_conquer_times = [measure_time(divide_and_conquer_power, 2, n) for n in exponents]
    
    sum_pairs_times = []
    for n in exponents:
        arr = list(range(2 * n))
        sum_pairs_times.append(measure_time(find_sum_pairs, arr, n))
    
    plot_results(exponents, naive_times, divide_conquer_times, sum_pairs_times)

run_experiments()
