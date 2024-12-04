from student import StudentInfo
from main_menu import MainMenu
from add_student import AddStudent
from search_student import SearchStudent
from print_all_students import PrintAllStudents
import os

student_info = StudentInfo()
add_stu = AddStudent(student_info)
search_stu = SearchStudent(student_info)
print_all = PrintAllStudents(student_info)
m_menu = MainMenu(add_stu, search_stu, print_all)

student_info.read_file()
attempts = 0
while attempts < 4:
    print("\n","="*10 , "Login - Student Info. System" , "="*10)
    login_check = input(f"\n>> Please enter your Student ID to continue: ")
    user = search_stu.verify_login(login_check)
    if user != False:  #Successful login
        os.system("cls")
        m_menu.main_menu(user)  #Show main menu
    else:
        attempts += 1  #Print number of attempts left
        os.system("cls")
        print(f"\n>> You only have {4 - attempts} attempts left.")
    if attempts > 3:
        os.system("cls")
        print("\n>> You have exceeded the number of attempts. L8r o7\n")