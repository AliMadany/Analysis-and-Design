import time

def naive(a, n): # loop runs n times so the time complexity is O(n).
    result = 1
    for i in range(n):
        result *= a
    return result

def DivConq(a, n): # Using Master thereom to calculate the time complexity, it's O(Log n)
    if n == 0:
        return 1
    if n % 2 == 0:
        half_power = DivConq(a, n // 2)
        return half_power * half_power
    else:
        half_power = DivConq(a, n // 2)
        return a * half_power * half_power
    
n_values = range(1, 10**6 + 1)  # Test with n from 1 to 10^6
naive_times = []
divide_and_conquer_times = []

for n in n_values:
    start_time = time.time()
    naive(2, n)  # Replace 2 with your desired base 'a'
    end_time = time.time()
    naive_times.append(end_time - start_time)

    start_time = time.time()
    DivConq(2, n)  # Replace 2 with your desired base 'a'
    end_time = time.time()
    divide_and_conquer_times.append(end_time - start_time)

