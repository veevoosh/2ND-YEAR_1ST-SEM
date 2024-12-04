arr = [1, 3, 5, 7, 9, 11, 13, 15]

# Credits: Geeks for Geeks (2023)

def binary_search(arr, target):
	low = 0
	high = len(arr) - 1
	mid = 0

	while low <= high:
		mid = (high + low) // 2
  
		if arr[mid] < target:
			low = mid + 1
   
		elif arr[mid] > target:
			high = mid - 1

		else:
			return mid
	return -1

print(f"\n>> The current array is:\n{arr}\n")

# Existing value in array (function call)
target = 7

result = binary_search(arr, target)

if result != -1:
	print(f">> Target Value: {target} | Index: " , str(result))
else:
	print(f">> Target Value: {target} | Index: -1")
 
# Not existing value in array (separate function call)
target = 4

result = binary_search(arr, target)

if result != -1:
	print(f">> Target Value: {target} | Index: " , str(result))
else:
	print(f">> Target Value: {target} | Index: -1")
 
print()