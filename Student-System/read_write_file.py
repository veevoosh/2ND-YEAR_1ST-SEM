def write_to_file(data_to_write):  #dont forget self if theres a class
    with open("student_data.txt", "a+") as file: #r, r+, or w,  rewrite EVERYTHING (no good) ... a+ is append
        for x in data_to_write:
            file.write(f"{x}")  #Sanity check (NOT FOR FORMATTING!!!! the frikken extra comma ...)
        file.write("\n")
        file.close()
    print("\n>> Student data added to the database!")

list_all = []
    
def read_file(self):
    try:
        with open("student_data.txt", "r") as file: #r for reading
            lines = file.readlines() #readLINES not readlinE
            for line in lines[0:]:
                list_all.append(line)
        print("\n>> Student data added to the list!")
    except FileNotFoundError:
        print("\n>> Oops! No existing student data found... sorz")

read_file()
print(list_all)