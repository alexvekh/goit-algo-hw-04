import timeit
import time
import copy
from functools import wraps

# алгоритм сортування вставками
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key
    print(lst)
    return lst

#алгоритм сортування злиттям
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

    # вібір та об'єднання менших елементів
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи вони додаються до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    return merged


# Define a decorator to measure time
def timeit(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    print(f"Average execution time of {func.__name__}: {(end_time - start_time):.6f} seconds")
    return result
  return wrapper
insertion_sort = timeit(insertion_sort)

numbers = [5, 3, 8, 4, 2]

# 4 copies for tests
numbers_copy1 = copy.deepcopy(numbers)
numbers_copy2 = copy.deepcopy(numbers)
numbers_copy3 = copy.deepcopy(numbers)
numbers_copy4 = copy.deepcopy(numbers)






print("\nCортування вставками")
print(f"unsorted list:".ljust(20), numbers_copy1)

# time_taken = timeit.timeit(stmt="insertion_sort(numbers_copy1)", number=100)
insertion_sorted = insertion_sort(numbers_copy1)
print(f"sorted by insertion".ljust(20), insertion_sorted)
# print(f"Average insertion sort time: {time_taken:.6f} seconds")

print("\nCортування методом злиття")
print(f"unsorted list:".ljust(20), numbers_copy2)
merge_sorted = merge_sort(numbers_copy2)
print("sorted by merge".ljust(20), merge_sorted)

print("\nCортування вбудованою функцєю sorted ")
print(f"unsorted list:".ljust(20), numbers_copy3)
sorted_sorted = sorted(numbers_copy3)
print("by sorted".ljust(20), sorted_sorted)

print("\nCортування вбудованою функцєю sort()")
print(f"unsorted list:".ljust(20), numbers_copy4)
numbers_copy4.sort()
print("by sort".ljust(20), numbers_copy4)

