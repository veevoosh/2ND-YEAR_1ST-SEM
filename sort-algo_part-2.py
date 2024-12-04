# Insertion Sort Activity

def insertion_sort(arr):
    counter = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        counter += 1
        print(f">> Sorted ({counter} Time/s):", arr)

# Activity: Test with a list

arr = [12, 11, 13, 5, 6]
print("\n>> Original Array:", arr)
insertion_sort(arr)
print()

# Merge Sort Activity

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        
        counter = 0
        
        while i < len(left_half) and j < len(right_half):
            counter += 1
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            print(f">> Sorted ({counter} Time/s):", arr)
        
        while i < len(left_half):
            counter += 1
            arr[k] = left_half[i]
            i += 1
            k += 1
            print(f">> Sorted ({counter} Time/s):", arr)
        
        while j < len(right_half):
            counter += 1
            arr[k] = right_half[j]
            j += 1
            k += 1
            print(f">> Sorted ({counter} Time/s):", arr)

# Activity: Test with a list

arr = [38, 27, 43, 3, 9, 82, 10]
print("\n>> Original Array:", arr , "\n")
merge_sort(arr)
print()
