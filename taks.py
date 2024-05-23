import timeit
import random

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def timsort(arr):
    return sorted(arr)

def measurement_time(func, arr):
    start_time = timeit.default_timer()
    func(arr)
    return timeit.default_timer() - start_time

sizes = [10, 100, 1000, 10000]
test_data = {size: [random.randint(0, 10000) for _ in range(size)] for size in sizes}

results = {
    'Insertion Sort': [],
    'Merge Sort': [],
    'Timsort': []
}

for size in sizes:
    data = test_data[size]
    
    data_copy = data.copy()
    time_insertion = measurement_time(insertion_sort, data_copy)
    results['Insertion Sort'].append(time_insertion)
    
    
    data_copy = data.copy()
    time_merge = measurement_time(merge_sort, data_copy)
    results['Merge Sort'].append(time_merge)
    
    data_copy = data.copy()
    time_timsort = measurement_time(timsort, data_copy)
    results['Timsort'].append(time_timsort)


for algo, times in results.items():
    print(f"{algo}:")
    for size, time_taken in zip(sizes, times):
        print(f"  Size {size}: {time_taken:.6f} seconds")

        