class StudentInfo():  #Holds the student list
    def __init__(self):
        self.name = ""
        self.age = ""
        self.id_num = ""
        self.email = ""
        self.phone_num = ""
        self.allstudents = []
    
    #Setters

    def setName(self, name):
        self.name = name
    
    def setAge(self, age):
        self.age = age
    
    def setIDNum(self, id_num):
        self.id_num = id_num
    
    def setEmail(self, email):
        self.email = email
    
    def setPhoneNum(self, phone_num):
        self.phone_num = phone_num
    
    #Getters

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

    def getIDNum(self):
        return self.id_num
    
    def getEmail(self):
        return self.email
    
    def getPhoneNum(self):
        return self.phone_num
    
    #__str__ method

    def __str__(self):
        print("\n" , "="*10 , "All Students' Information" , "="*10)
        for student in self.allstudents:
            print(f"Name: {student[0]}\nAge: {student[1]}\nID Number: {student[2]}\nEmail: {student[3]}\nPhone Number: {student[4]}\n")
        print("\n" , "="*10 , "Nothing Follows" , "="*10)
    
    def read_file(self):
        try:
            with open("student_data.txt", "r") as file: #r for reading
                lines = file.readlines() #readLINES not readlinE
                for line in lines[0:]:
                    self.allstudents.append(line.split(", "))  #THANK YOU BEKAH WERHHGGHRHHHFHDG (10/15/2024) REMEMBER SPLIT!~!~!~!!!
            print("\n>> The student data is added to the list!")
        except FileNotFoundError:
            print("\n>> Sorry! No existing student data found... :[c")