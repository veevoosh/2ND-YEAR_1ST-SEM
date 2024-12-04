# Activity 1

arr = [10, 20, 30, 40, 50]

def insert():
    new_el = int(input("Please enter a number you wish to add to the array: "))
    arr.append(new_el)
    print(">>" , new_el , "has been added to the array.")

def delete():
    del_el = int(input("Please enter the number you wish to delete from the array: "))
    arr.remove(del_el)
    print(">>" , del_el , "has been deleted from the array.")

def display():
    print(">> Here are all of the elements of the array:")
    print(arr)
    
# Supplemental Activity for Activity 1

def search():
    search_el = int(input("Please enter the number you wish to search in the array: "))
    if search_el in arr:
        print("The index of" , search_el , "is:")
        print(">>" , arr.index(search_el))
    else:
        print(">> NOT FOUND")

insert()
delete()
display()
search()
