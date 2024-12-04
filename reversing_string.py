# All credits to  Sunny Karira from GeeksforGeeks (2023)

def createStack():
	stack = []
	return stack

def size(stack):
	return len(stack)

def isEmpty(stack):
	if size(stack) == 0:
		return True

def push(stack, item):
	stack.append(item)

def pop(stack):
	if isEmpty(stack):
		return
	return stack.pop()

def reverse(string):
	n = len(string)

	stack = createStack()

	for i in range(0, n, 1):
		push(stack, string[i])

	string = ""

	for i in range(0, n, 1):
		string += pop(stack)

	return string

string = "Reversing String Using Stack"
print(f">> The original string is '{string}'\n")
print(f">> The reversed string is '{reverse(string)}'\n")
