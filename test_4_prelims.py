import os  # For 'os.system()' use

numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'e']
nerds = ['Ford', 'Stan', 'Bill', 'Dipper', 'Mabel']

class Options():
    def main_menu(self):  # TypeError: Options.main_menu() takes 0 positional arguments but 1 was given
                          # Fix: Add 'self' as argument to method
        while True:
            print("\n", "="*5, "Main Menu", "="*5)
            choice = input("\n[1] Insert a new element at the end\n[2] Delete an element\n[3] Search for an element\n[4] Insert a new element in a specific index\n[5] Sort in ascending order\n[6] Sort in reverse order\n[7] Slice in 2nd to the 4th element (inclusive)\n[8] Quit the program\n\n>> Enter your choice: ")
            if choice == '1':
                os.system("cls")  # Clears terminal screen
                Options.insert()
            elif choice == '2':
                os.system("cls")
                Options.delete()
            elif choice == '3':
                os.system("cls")
                Options.search()
            elif choice == '4':
                os.system("cls")
                Options.insert_specific()
            elif choice == '5':
                os.system("cls")
                Options.ascending()
            elif choice == '6':
                os.system("cls")
                Options.reverse()
            elif choice == '7':
                os.system("cls")
                Options.slice()
            elif choice == '8':
                print("\n>> Goodbye! Thank you for using the program!")
                print()
                exit()
                break
            else:
                print("\n>> Sorry! That choice is NOT in the list.\n>> Please try again! :D\n")
                continue  # Go back to Main Menu

    def insert():
        while True:
            arr = input("\n>> Please choose an array to edit:\n[1] Numbers\n[2] Letters\n[3] Nerds\n\n>> Enter your choice: ")
            if arr == '1':
                new = int(input("\n>> Enter a new element to add to the array: "))  # Use 'int' for Integers
                numbers.append(new)  # Use ACTUAL name of array/list instead of renaming them
                print(f"\n>> Element '{new}' has been added to the array!")
                print(numbers)
                return False
            elif arr == '2':
                new = input("\n>> Enter a new element to add to the array: ")
                letters.append(new)
                print(f"\n>> Element '{new}' has been added to the array!")
                print(letters)
                return False
            elif arr == '3':
                new = input("\n>> Enter a new element to add to the array: ")
                nerds.append(new)
                print(f"\n>> Element '{new}' has been added to the array!")
                print(nerds)
                return False
            else:
                print("\n>> Sorry! That array is NOT in the list.\n>> Please try again! :D")
                return False
    
    def delete():
        while True:
            arr = input("\n>> Please choose an array to edit:\n[1] Numbers\n[2] Letters\n[3] Nerds\n\n>> Enter your choice: ")
            if arr == '1':
                new = int(input("\n>> Enter an element to delete from the array: "))
                numbers.remove(new)
                print(f">> Element '{new}' has been deleted from the array!")
                print(numbers)
                return False
            elif arr == '2':
                new = input("\n>> Enter an element to delete from the array: ")
                letters.remove(new)
                print(f"\n>> Element '{new}' has been deleted from the array!")
                print(letters)
                return False
            elif arr == '3':
                new = input("\n>> Enter an element to delete from the array: ")
                nerds.remove(new)
                print(f"\n>> Element '{new}' has been deleted from the array!")
                print(nerds)
                return False
            else:
                print("\n>> Sorry! That array is NOT in the list. Please try again! :D")
                return False

    def search():
        while True:
            arr = input("\n>> Please choose an array to search for elements:\n[1] Numbers\n[2] Letters\n[3] Nerds\n\n>> Enter your choice: ")
            if arr == '1':
                new = int(input("\n>> Enter an element to search in the array: "))
                if new in numbers:
                    print(f"\n>> Element '{new}' is in index [{numbers.index(new)}] in the array!")
                    print(numbers)
                    return False
                else:
                    print(f"\n>> Element '{new}' is NOT FOUND in the array!")
                    return False
            elif arr == '2':
                new = input("\n>> Enter an element to search in the array: ")
                if new in letters:
                    print(f"\n>> Element '{new}' is in index [{letters.index(new)}] in the array!")
                    print(letters)
                    return False
                else:
                    print(f"\n>> Element '{new}' is NOT FOUND in the array!")
                    return False
            elif arr == '3':
                new = input("\n>> Enter an element to search in the array: ")
                if new in nerds:
                    print(f"\n>> Element '{new}' is in index [{nerds.index(new)}] in the array!")
                    print(nerds)
                    return False
                else:
                    print(f"\n>> Element '{new}' is NOT FOUND in the array!")
                    return False
            else:
                print("\n>> Sorry! That array is NOT in the list. Please try again! :D")
                return False
    
    def insert_specific():
        while True:
            arr = input("\n>> Please choose an array to edit:\n[1] Numbers\n[2] Letters\n[3] Nerds\n\n>> Enter your choice: ")
            if arr == '1':
                new = int(input("\n>> Enter a new element to add to the array: "))
                spot = int(input("\n>> Enter the index where you would like to add the element in the array: "))
                numbers.insert(spot, new)
                print(f"\n>> Element '{new}' has been added to the array!")
                print(numbers)
                return False
            elif arr == '2':
                new = input("\n>> Enter a new element to add to the array: ")
                spot = int(input("\n>> Enter the index where you would like to add the element in the array: "))
                letters.insert(spot, new)
                print(f"\n>> Element '{new}' has been added to the array!")
                print(letters)
                return False
            elif arr == '3':
                new = input("\n>> Enter a new element to add to the array: ")
                spot = int(input("\n>> Enter the index where you would like to add the element in the array: "))
                nerds.insert(spot, new)
                print(f"\n>> Element '{new}' has been added to the array!")
                print(nerds)
                return False
            else:
                print("\n>> Sorry! That array is NOT in the list.\n>> Please try again! :D")
                return False

    def ascending():
        while True:
            arr = input("\n>> Please choose an array to sort:\n[1] Numbers\n[2] Letters\n[3] Nerds\n\n>> Enter your choice: ")
            if arr == '1':
                numbers.sort()
                print(f"\n>> Edited list in ascending order: {numbers}")
                return False
            elif arr == '2':
                letters.sort()
                print(f"\n>> Edited list in ascending order: {letters}")
                return False
            elif arr == '3':
                nerds.sort()
                print(f"\n>> Edited list in ascending order: {nerds}")
                return False
            else:
                print("\n>> Sorry! That array is NOT in the list.\n>> Please try again! :D")
                return False
    
    def reverse():
        while True:
            arr = input("\n>> Please choose an array to sort:\n[1] Numbers\n[2] Letters\n[3] Nerds\n\n>> Enter your choice: ")
            if arr == '1':
                numbers.sort(reverse=True)
                print(f"\n>> Edited list in reverse order: {numbers}")
                return False
            elif arr == '2':
                letters.sort(reverse=True)
                print(f"\n>> Edited list in reverse order: {letters}")
                return False
            elif arr == '3':
                nerds.sort(reverse=True)
                print(f"\n>> Edited list in reverse order: {nerds}")
                return False
            else:
                print("\n>> Sorry! That array is NOT in the list.\n>> Please try again! :D")
                return False
    
    def slice():
        while True:
            arr = input("\n>> Please choose an array to sort:\n[1] Numbers\n[2] Letters\n[3] Nerds\n\n>> Enter your choice: ")
            if arr == '1':
                numbers.sort()
                print(f"\n>> Edited list in sliced order: {numbers[1:4]}")
                return False
            elif arr == '2':
                letters.sort()
                print(f"\n>> Edited list in sliced order: {letters[1:4]}")
                return False
            elif arr == '3':
                nerds.sort()
                print(f"\n>> Edited list in sliced order: {nerds[1:4]}")
                return False
            else:
                print("\n>> Sorry! That array is NOT in the list.\n>> Please try again! :D")
                return False

test_program = Options()

if __name__ == '__main__':
    test_program.main_menu()