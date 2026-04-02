#Task 1: Use super() properly
# Base class
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(f"Name: {self.name}, ID: {self.id}")


# Child class: Student
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def display(self):
        super().display()
        print(f"Department: {self.dept}, Fees: {self.fees}")


# Child class: Faculty
class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def display(self):
        super().display()
        print(f"Salary: {self.salary}")


# Child class: TempFaculty (inherits from Faculty)
class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def display(self):
        super().display()
        print(f"Duration: {self.duration} months")


# Creating objects
s = Student("Alice", 101, "Computer Science", 50000)
f = Faculty("Bob", 201, 80000)
t = TempFaculty("Charlie", 301, 40000, 6)

# Display details
print("Student Details:")
s.display()

print("\nFaculty Details:")
f.display()

print("\nTemporary Faculty Details:")
t.display()

#Task 2:Apply Abstraction
from abc import ABC, abstractmethod

# Abstract base class
class AbstractUser(ABC):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    @abstractmethod
    def get_details(self):
        pass


# Child class: Student
class Student(AbstractUser):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"Student -> Name: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"


# Child class: Faculty
class Faculty(AbstractUser):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"Faculty -> Name: {self.name}, ID: {self.id}, Salary: {self.salary}"


# Child class: TempFaculty
class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self):
        return f"TempFaculty -> Name: {self.name}, ID: {self.id}, Salary: {self.salary}, Duration: {self.duration} months"


# Creating objects
s = Student("Alice", 101, "Computer Science", 50000)
f = Faculty("Bob", 201, 80000)
t = TempFaculty("Charlie", 301, 40000, 6)

# Display details
print(s.get_details())
print(f.get_details())
print(t.get_details())

#Task 3: Sorting using key
# Student class
class Student:
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees

    def __repr__(self):
        return f"{self.name} (Fees: {self.fees})"


# Faculty class
class Faculty:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def __repr__(self):
        return f"{self.name} (Salary: {self.salary})"


# Creating lists
students = [
    Student("Alice", 101, "CS", 50000),
    Student("Bob", 102, "IT", 30000),
    Student("Charlie", 103, "ECE", 40000)
]

faculty = [
    Faculty("Dr. Smith", 201, 90000),
    Faculty("Dr. John", 202, 70000),
    Faculty("Dr. Lee", 203, 80000)
]

# Sorting
students.sort(key=lambda x: x.fees)
faculty.sort(key=lambda x: x.salary)

# Display sorted results
print("Students sorted by fees:")
for s in students:
    print(s)

print("\nFaculty sorted by salary:")
for f in faculty:
    print(f)
    
#Task 4: Use map()   

# Student class
class Student:
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees

    def __repr__(self):
        return f"{self.name} ({self.dept})"


# Creating a list of students
students = [
    Student("Alice", 101, "CS", 50000),
    Student("Bob", 102, "IT", 30000),
    Student("Charlie", 103, "ECE", 40000)
]

# Using map() to extract names
names = list(map(lambda s: s.name, students))

# Display results
print("Student Objects:")
for s in students:
    print(s)

print("\nExtracted Names:")
print(names)

#Task 5: Use filter()

# Student class
class Student:
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees

    def __repr__(self):
        return f"{self.name} (Fees: {self.fees})"


# Faculty class
class Faculty:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def __repr__(self):
        return f"{self.name} (Salary: {self.salary})"


# Creating lists
students = [
    Student("Alice", 101, "CS", 60000),
    Student("Bob", 102, "IT", 30000),
    Student("Charlie", 103, "ECE", 70000)
]

faculty = [
    Faculty("Dr. Smith", 201, 25000),
    Faculty("Dr. John", 202, 40000),
    Faculty("Dr. Lee", 203, 35000)
]

# Using filter()
high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))

# Display results
print("Students with fees > 50000:")
for s in high_fee_students:
    print(s)

print("\nFaculty with salary > 30000:")
for f in high_salary_faculty:
    print(f)
    
#Task 6: Use reduce()

from functools import reduce

# Student class
class Student:
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees


# Faculty class
class Faculty:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary


# Creating lists
students = [
    Student("Alice", 101, "CS", 50000),
    Student("Bob", 102, "IT", 30000),
    Student("Charlie", 103, "ECE", 40000)
]

faculty = [
    Faculty("Dr. Smith", 201, 90000),
    Faculty("Dr. John", 202, 70000),
    Faculty("Dr. Lee", 203, 80000)
]

# Using reduce()
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

# Display results
print("Total Fees Collected:", total_fees)
print("Total Salary of Faculty:", total_salary)  

#Task 7: Higher Order Function

# Student class
class Student:
    def __init__(self, name, id, dept, fees):
        self.name = name
        self.id = id
        self.dept = dept
        self.fees = fees

    def __repr__(self):
        return f"{self.name} ({self.dept}, Fees: {self.fees})"


# Higher Order Function
def process_users(users, func):
    return list(map(func, users))


# Creating list of students
students = [
    Student("Alice", 101, "CS", 50000),
    Student("Bob", 102, "IT", 30000),
    Student("Charlie", 103, "ECE", 40000)
]

# Function to extract names
def get_name(user):
    return user.name

# Function to increase fees by 10%
def increase_fees(user):
    user.fees = int(user.fees * 1.1)
    return user

# Applying higher order function
names = process_users(students, get_name)
updated_students = process_users(students, increase_fees)

# Display results
print("Student Names:")
print(names)

print("\nStudents after fee increase:")
for s in updated_students:
    print(s)
    
#Final Challenge    

from abc import ABC, abstractmethod
from functools import reduce

# Abstract Base Class
class AbstractUser(ABC):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    @abstractmethod
    def get_details(self):
        pass


# Student Class
class Student(AbstractUser):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"Student -> {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"


# Faculty Class
class Faculty(AbstractUser):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"Faculty -> {self.name}, ID: {self.id}, Salary: {self.salary}"


# Data
students = [
    Student("Alice", 101, "CS", 60000),
    Student("Bob", 102, "IT", 30000),
    Student("Charlie", 103, "ECE", 70000)
]

faculty = [
    Faculty("Dr. Smith", 201, 25000),
    Faculty("Dr. John", 202, 40000),
    Faculty("Dr. Lee", 203, 35000)
]

# 1. Print all details (map)
print("All Student Details:")
student_details = list(map(lambda s: s.get_details(), students))
for d in student_details:
    print(d)

print("\nAll Faculty Details:")
faculty_details = list(map(lambda f: f.get_details(), faculty))
for d in faculty_details:
    print(d)

# 2. Sorting (key)
students.sort(key=lambda s: s.fees)
faculty.sort(key=lambda f: f.salary)

print("\nStudents Sorted by Fees:")
for s in students:
    print(s.get_details())

print("\nFaculty Sorted by Salary:")
for f in faculty:
    print(f.get_details())

# 3. Filtering (filter)
high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))

print("\nHigh Fee Students (>50000):")
for s in high_fee_students:
    print(s.get_details())

print("\nHigh Salary Faculty (>30000):")
for f in high_salary_faculty:
    print(f.get_details())

# 4. Aggregation (reduce)
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

print("\nTotal Fees Collected:", total_fees)
print("Total Salary Paid:", total_salary)