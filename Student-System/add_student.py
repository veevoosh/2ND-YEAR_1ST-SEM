import os

class AddStudent():
    def __init__(self, student):  #Need to study how this works!!!
        self.student_data = student
    
    def add_student(self):  #Put getters and setters...
        while True:
            print("\n","="*10 , "Add New Student" , "="*10, "\n")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            id_num = input("Enter Student ID: ")
            email = input("Enter Email Address: ")
            phone_num = input("Enter Phone Number: ")
            student = name, age, id_num, email, phone_num
            self.student_data.allstudents.append(student) 
            print("\n","="*10 , "Nothing Follows" , "="*10)
            print(f"\n>> Added student {name} to the record.")
            self.write_to_file(f"\n{name}, {age}, {id_num}, {email}, {phone_num}")  #Fixed the silly formatting !! THANKS MARJ!!
            check = input("\n>> Do you want to try again? [Y/N]: ")
            if check.lower() != 'y':
                os.system("cls")
                break
            else:
                os.system("cls")
    
    def write_to_file(self, data_to_write):
        with open("student_data.txt", "a+") as file: #NOT 'w" !!!!!!!
            for x in data_to_write:
                file.write(x)
            file.close()  #ALWAYS CLOSE !!!
        print("\n>> Data saved successfully! Yippee! :D")