# Activity 3

letters = ['a','b','c','d','e']

def insert():
    print(letters , "\n")
    new_letter = 'z'
    letters.insert(6, new_letter)
    print(letters , "\n")
    print(">>" , "'" + new_letter + "'" , "has been added to the array.\n")

def remove():
    print(letters , "\n")
    del_letter = 'b'
    letters.remove(del_letter)
    print(">>" , "'" + del_letter + "'" , "has been deleted from the array.\n")
    print(letters , "\n")

def search():
    search_letter = 'z'
    if search_letter in letters:
        print(">> The index of" , "'" + search_letter + "'" , "is:" , letters.index(search_letter) , "\n")
        print(letters , "\n")
    else:
        print(">>" , search_letter , "is NOT FOUND!\n")
        print(letters , "\n")

insert()
remove()
search()
