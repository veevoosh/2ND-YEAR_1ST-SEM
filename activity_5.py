arr = [2, 4, 6, 8, 10, 12, 14]

# I reused code from my previous activity as reference

def linear_search(arr, target):
    if target in arr:
        print(f">> Target Value: {target} | Index: " , arr.index(target))
    else:
        print(f">> Target Value: {target} | Index: -1")

print(f"\n>> The current array is:\n{arr}\n")

# Existing value in array (function call)
linear_search(arr, 6)

# Not existing value in array (separate function call)
linear_search(arr, 7)

print()