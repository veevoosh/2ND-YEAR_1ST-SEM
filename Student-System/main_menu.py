import os

class MainMenu():
    def __init__(self, add_stu, search_stu, print_all):
        self.add_stu = add_stu
        self.search_stu = search_stu
        self.print_all = print_all
    
    def main_menu(self, user):
        while True:
            print(f"\n>> Welcome, {user[0]}!")
            print("\n","="*10 , "Main Menu" , "="*10)
            print("\n[1] View your information\n[2] View other student's information\n[3] Register a new student\n[4] Print all students in the system\n[5] Exit the system")
            choice = int(input("\n>> Enter your choice: "))
            if choice == 1:
                os.system("cls")
                search = user[1]
                self.search_stu.search_student(search)
            elif choice == 2:
                os.system("cls")
                search = input("\n>> Enter Student ID to search: ")
                self.search_stu.search_student(search)
            elif choice == 3:
                os.system("cls")
                self.add_stu.add_student()
            elif choice == 4:
                os.system("cls")
                self.print_all.print_all_students()
            elif choice == 5:
                os.system("cls")
                print("\n>> Exiting the system... Cya o/")
                print()
                exit()
                break
            else:
                os.system("cls")
                print("\n","="*6 , "Oops, try again :P" , "="*6)
                continue