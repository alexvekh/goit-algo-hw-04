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

def merge_k_lists(lists):
    left = lists.pop()
    for right in lists:
        # print("L", left, 'R', right, 'all', list)
        left = merge(left, right)   
    return left


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)