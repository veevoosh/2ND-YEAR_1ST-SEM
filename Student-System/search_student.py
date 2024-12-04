class SearchStudent():
    def __init__(self, student):  #Need to study how this works!!!
        self.student_data = student
    
    def search_student(self, student_id):
        for student in self.student_data.allstudents:
            if student_id == student[2]:
                print("\n" , "="*8 , "Students' Information" , "="*8)
                print(f"\nName: {student[0]}\nAge: {student[1]}\nID Number: {student[2]}\nEmail: {student[3]}\nPhone Number: {student[4]}")
                print("="*10 , "Nothing Follows" , "="*10)
                return
        else:
            print("\n" , "="*8 , "Students' Information" , "="*8)
            print(f"\n>> Oops, sorry! Looks like the student with the ID '{student_id}' does not exist!")
            print("\n" , "="*10 , "Nothing Follows" , "="*10)
    
    def verify_login(self, student_id):
        for student in self.student_data.allstudents:
            if student[2] == student_id:
                return [student[0], student[2]]  #Or 'return student'
        return False