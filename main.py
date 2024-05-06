import timeit
import copy
import random

# алгоритм сортування вставками
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key
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


small_list = [34, 12, 90, 5, 18, 77, 23, 66, 41, 8]
reserved_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] # for test worse case
with_dublikans_list = [34, 8, 12, 66, 90, 5, 18, 77, 23, 66, 41, 5, 8]
letters = ['a', 'h', 'z', 'q', 'u', 'b', 'c', 'w', 'd']
big_list = [random.randint(1, 5000) for _ in range(500)]



number_lists = [small_list, reserved_list, with_dublikans_list, letters, big_list]
letters = ['a', 'h', 'q', 'u', 'b']

for numbers in number_lists:
  
    print('-'*70)
    print(numbers)
    print("\nCортування вставками")
    numbers_copy = copy.deepcopy(numbers)
    print(f"  unsorted:".ljust(20), numbers_copy)
    print(f"  sorted by insertion:".ljust(20), insertion_sort(numbers_copy))

    def sort_by_insertion():
        numbers_copy = copy.deepcopy(numbers)    
        insertion_sort(numbers_copy)

    time_taken = timeit.timeit(sort_by_insertion, number=1000) / 1000
    print(f"Average insertion sort time: {time_taken:.6f} seconds")

    print("\nCортування методом злиття")
    numbers_copy = copy.deepcopy(numbers)
    print(f"  unsorted:".ljust(20), numbers_copy)
    print(f"  sorted by merge:".ljust(20), merge_sort(numbers_copy))

    def sort_by_merge():
        numbers_copy = copy.deepcopy(numbers)
        merge_sort(numbers_copy)

    time_taken = timeit.timeit(sort_by_merge, number=1000) / 1000
    print(f"Average merge_sort time: {time_taken:.6f} seconds")

    print("\nCортування вбудованою функцєю sorted ")
    numbers_copy = copy.deepcopy(numbers)
    print(f"  unsorted:".ljust(20), numbers_copy)
    print(f"  sorted by sorted:".ljust(20), sorted(numbers_copy))

    def sort_by_sorted():
        numbers_copy = copy.deepcopy(numbers)
        sorted(numbers_copy)

    time_taken = timeit.timeit(sort_by_sorted, number=1000) / 1000
    print(f"Average sorted time: {time_taken:.6f} seconds")

    print("\nCортування вбудованою функцєю sort()")
    numbers_copy = copy.deepcopy(numbers)
    print(f"  unsorted:".ljust(20), numbers_copy)
    numbers_copy.sort()
    print(f"  sorted by .sort():".ljust(20), numbers_copy)

    def sort_by_sort():
        numbers_copy = copy.deepcopy(numbers)
        numbers_copy.sort()

    time_taken = timeit.timeit(sort_by_sort, number=1000) / 1000
    print(f"Average .sort() time: {time_taken:.6f} seconds")

"""
Тестування алгоритмів сортування (сотрування вставками, сортування злиттям, та внутрішніх функцій Timsort (sort() sorted)) 
на різних масивах даних (малий список(10), зворотній список(10), список з дублікатими(12), список з букв(9) великий список(500))
показало що sort() та sorted покзує кращі результати на всіх тестованих списках, особливо на великому списку.
  - малий список внутрішні функції сортують в 2 рази швидше
  - зворотній список в 2.6 рази швидше
  - список з дублікатими в 2.1 рази швидше за сортуваня злиттям, але не суттєво швидше за сотрування вставками
  - список з букв в 2.75 рази швидше
  - великий список в 14 зазів швидше. Проте найшірше з великим списком працює сотрування вставками. 
    Сортування злиттям в 4,75 разів швидше, а .sort() в 24.
"""