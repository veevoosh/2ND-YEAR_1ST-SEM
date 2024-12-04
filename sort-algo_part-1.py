# Bubble Sort Activity

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

# Activity: Test with a list

arr = [5, 1, 4, 2, 8]
print("\n>> Original Array:", arr)
print(">> Sorted (1st):", bubble_sort(arr))
print(">> Sorted (2nd):", bubble_sort(arr))
print(">> Sorted (3rd):", bubble_sort(arr))
print(">> Sorted (4th):", bubble_sort(arr))
print(">> Sorted (5th):", bubble_sort(arr))
print()

# Selection Sort Activity

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i 
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Activity: Test with a list

arr_1 = [29, 10, 14, 37, 13]
print("\n>> Original Array:", arr_1)
print(">> Sorted Array:", selection_sort(arr_1))

arr_2 = ['Rita', 'Deborah', 'Matthews', 'Doakes', 'Chutsky', 'Dexter']
print("\n>> Original Array:", arr_2)
print(">> Sorted Array:", selection_sort(arr_2))
print()