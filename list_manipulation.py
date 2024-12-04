# Activity 2

my_list = [12, 3, 5, 22, 25]

def ascending():
    my_list.sort()
    print(my_list)

def reverse():
    my_list.sort(reverse=True)
    print(my_list)

def slice_o_pie():
    my_list.sort()
    print(my_list[1:4])
    
ascending()
reverse()
slice_o_pie()
