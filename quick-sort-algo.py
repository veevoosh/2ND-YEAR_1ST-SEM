def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 10]
    print(f"\n>> The current pivot selection is '{pivot}'")
    left = [x for x in arr if x < pivot]
    print(f">> The left selection is {left}")
    middle = [x for x in arr if x == pivot]
    print(f">> The middle selection is {middle}")
    right = [x for x in arr if x > pivot]
    print(f">> The right selection is {right}")
    return quick_sort(left) + middle + quick_sort(right)

# Activity: Test with a list
arr = [10, 7, 8, 9, 1, 5]
print("\n>> Original:", arr)
print("\n>> Sorted:", quick_sort(arr) , "\n")
