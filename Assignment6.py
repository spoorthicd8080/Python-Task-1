#Task 1: Encapsulation (User Class)

class User:
    def __init__(self):
        self.__user_name = None   
        self.__pwd = None        

    # setter method
    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    # getter method (only username, password hidden)
    def get_user(self):
        return self.__user_name

    # register method
    def register(self):
        print(f"Registering user: {self.__user_name}")

    # login method
    def login(self):
        print(f"Logging in: {self.__user_name}")


# Creating object
user1 = User()

# Setting user details
user1.set_user("john", "1234")

# Calling methods
user1.register()
user1.login()

#Task 2: Inheritance (User → Student, Faculty)

# Parent Class
class User:
    def register(self):
        print("User registered")

    def login(self):
        print("User logged in")


# Child Class: Student
class Student(User):
    def student_greet(self):
        print("Hello Student")


# Child Class: Faculty
class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")


# Multilevel Inheritance: TempFaculty inherits from Faculty
class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")


# Creating objects
student = Student()
faculty = Faculty()
temp_faculty = TempFaculty()
user = User()


# Calling methods

print("---- Student Object ----")
student.register()          
student.login()             
student.student_greet()     

print("\n---- Faculty Object ----")
faculty.register()          
faculty.login()             
faculty.faculty_greet()    

print("\n---- TempFaculty Object ----")
temp_faculty.register()         
temp_faculty.login()            
temp_faculty.faculty_greet()    
temp_faculty.tempFaculty_greet()

print("\n---- User Object ----")
user.register()
user.login()

# Task 3: Method Overriding

# Parent Class
class User:
    def greet(self):
        print("Welcome User")


# Child Class: Student
class Student(User):
    def greet(self):   
        print("Welcome Student")


# Child Class: Faculty
class Faculty(User):
    def greet(self):   
        print("Welcome Faculty")


# Creating objects
student = Student()
faculty = Faculty()
user = User()

# Calling greet() method
print("---- Method Overriding Output ----")
student.greet()
faculty.greet()
user.greet()

#Task 4: Method Chaining

class User:
    def register(self):
        print("registered")
        return self   

    def login(self):
        print("logined")
        return self   

    def greet(self):
        print("enjoy everyone")
        return self   


# Creating object
user = User()

# Method chaining
user.login().greet().register()

#Task 5: Combined Task (Real-Time)

# Parent Class
class User:
    users_count = 0   

    def __init__(self, user_name, pwd):
        self.__user_name = user_name   
        self.__pwd = pwd               
        User.users_count += 1

    # getter (only username)
    def get_user(self):
        return self.__user_name

    # method chaining methods
    def register(self):
        print(f"{self.__user_name} registered")
        return self

    def login(self):
        print(f"{self.__user_name} logined")
        return self

    def greet(self):
        print("Welcome User")
        return self


# Child Class: Student
class Student(User):
    def greet(self):   
        print("Welcome Student")
        return self


# Child Class: Faculty
class Faculty(User):
    def greet(self):   
        print("Welcome Faculty")
        return self

# Creating objects
student = Student("john", "1234")
faculty = Faculty("alice", "abcd")

# Method chaining
print("---- Student ----")
student.login().greet().register()

print("\n---- Faculty ----")
faculty.login().greet().register()

# Total users created
print("\nTotal Users:", User.users_count)