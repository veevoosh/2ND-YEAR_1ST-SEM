class PrintAllStudents():
    def __init__(self, student):  #Need to study how this works!!!
        self.student_data = student

    def print_all_students(self):
            print("\n" , "="*8 , "All Students' Information" , "="*8, "\n")
            for student in self.student_data.allstudents:
                print(f"Name: {student[0]}\nAge: {student[1]}\nID Number: {student[2]}\nEmail: {student[3]}\nPhone Number: {student[4]}\n")
            print("="*10 , "Nothing Follows" , "="*10)