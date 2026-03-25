# Mini Project1: Employee Management System

employees = []

# Add new employee
def add_employee():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    role = input("Enter role: ")
    salary = float(input("Enter salary: "))

    emp = {
        "name": name,
        "age": age,
        "role": role,
        "salary": salary
    }

    employees.append(emp)
    print("Employee added successfully!\n")


# Display all employees
def display_employees():
    if not employees:
        print("No employees found.\n")
        return

    print("\nEmployee List:")
    for i, emp in enumerate(employees):
        print(f"{i + 1}. Name: {emp['name']}, Age: {emp['age']}, Role: {emp['role']}, Salary: {emp['salary']}")
    print()


# Update employee details
def update_employee():
    display_employees()
    if not employees:
        return

    index = int(input("Enter employee number to update: ")) - 1

    if 0 <= index < len(employees):
        print("Leave blank to keep old value")

        name = input("Enter new name: ")
        age = input("Enter new age: ")
        role = input("Enter new role: ")
        salary = input("Enter new salary: ")

        if name:
            employees[index]["name"] = name
        if age:
            employees[index]["age"] = int(age)
        if role:
            employees[index]["role"] = role
        if salary:
            employees[index]["salary"] = float(salary)

        print("Employee updated successfully!\n")
    else:
        print("Invalid employee number!\n")


# Delete employee
def delete_employee():
    display_employees()
    if not employees:
        return

    index = int(input("Enter employee number to delete: ")) - 1

    if 0 <= index < len(employees):
        removed = employees.pop(index)
        print(f"Employee {removed['name']} deleted successfully!\n")
    else:
        print("Invalid employee number!\n")


# Main menu
def main():
    while True:
        print("===== Employee Management System =====")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            display_employees()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.\n")


# Run program
main()

# Mini Project2: # Student Report Card Card

# Function to calculate grade
def calculate_grade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 75:
        return 'A'
    elif avg >= 60:
        return 'B'
    elif avg >= 50:
        return 'C'
    else:
        return 'F'

# Function to create report card
def report_card():
    student = {}

    student["name"] = input("Enter student name: ")
    student["marks"] = []

    # Input marks for 3 subjects
    for i in range(1, 4):
        mark = float(input(f"Enter marks for subject {i}: "))
        student["marks"].append(mark)

    total = sum(student["marks"])
    average = total / 3
    grade = calculate_grade(average)

    # Display formatted report
    print("\n------ Report Card ------")
    print(f"Name     : {student['name']}")
    print(f"Marks    : {student['marks']}")
    print(f"Total    : {total}")
    print(f"Average  : {average:.2f}")
    print(f"Grade    : {grade}")
    print("-------------------------")

# Run program
report_card()

#Mini project3: Shopping Cart System

cart = []

# Add product
def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    cart.append(product)
    print("Product added to cart!\n")


# Display cart
def display_cart():
    if not cart:
        print("Cart is empty.\n")
        return

    print("\n----- Shopping Cart -----")
    total = 0

    for i, item in enumerate(cart):
        item_total = item["price"] * item["quantity"]
        total += item_total

        print(f"{i+1}. {item['name']} | Price: {item['price']} | Qty: {item['quantity']} | Total: {item_total}")

    print("--------------------------")
    print(f"Total Bill: {total}\n")


# Remove product
def remove_product():
    display_cart()
    if not cart:
        return

    index = int(input("Enter item number to remove: ")) - 1

    if 0 <= index < len(cart):
        removed = cart.pop(index)
        print(f"{removed['name']} removed from cart.\n")
    else:
        print("Invalid choice!\n")


# Main menu
def main():
    while True:
        print("===== Shopping Cart Menu =====")
        print("1. Add Product")
        print("2. Display Cart")
        print("3. Remove Product")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_product()
        elif choice == '2':
            display_cart()
        elif choice == '3':
            remove_product()
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice!\n")


# Run program
main()

#Mini Project 4: #Login & User Validation
# Login & User Validation System

# Stored users (username: password)
users = {
    "admin": "admin123",
    "john": "john123",
    "alice": "alice456"
}

# Login function
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Validate credentials
    if username in users and users[username] == password:
        print("Login Successful! Welcome,", username)
    else:
        print("Login Failed! Invalid username or password.")

# Run program
login()

#Mini Project 5: Unique Visitor Counter
# Unique Visitor Counter

visitors = set()

def add_visitors():
    n = int(input("Enter number of visitors: "))

    for i in range(n):
        name = input(f"Enter visitor {i+1} name: ")
        visitors.add(name)   # set automatically avoids duplicates

def display_visitors():
    print("\nUnique Visitors:")
    for v in visitors:
        print(v)

    print(f"\nTotal Unique Visitors: {len(visitors)}")

# Run program
add_visitors()
display_visitors()

#Mini Project 6: String Formatter Tool
# String Formatter Tool

def formatter():
    name = input("Enter your name: ")
    product = input("Enter product name: ")

    # Formatted sentence
    print("\nFormatted Sentence:")
    print(f"{name} purchased a {product}.")

    # Padding examples
    print("\nPadded Output:")
    print("Left aligned  : {:<20}".format(name))
    print("Right aligned : {:>20}".format(name))
    print("Center aligned: {:^20}".format(name))

# Run program
formatter()

#Mini Project 7: Bank Account System
# Bank Account System

account = {}

# Create account
def create_account():
    name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))

    account["name"] = name
    account["balance"] = balance

    print("Account created successfully!\n")


# Deposit money
def deposit():
    amount = float(input("Enter amount to deposit: "))
    account["balance"] += amount
    print(f"Deposited {amount} successfully!\n")


# Withdraw money
def withdraw():
    amount = float(input("Enter amount to withdraw: "))

    if amount <= account["balance"]:
        account["balance"] -= amount
        print(f"Withdrawn {amount} successfully!\n")
    else:
        print("Insufficient balance!\n")


# Check balance
def check_balance():
    print("\n----- Account Details -----")
    print(f"Name    : {account.get('name')}")
    print(f"Balance : {account.get('balance')}")
    print("----------------------------\n")


# Main menu
def main():
    while True:
        print("===== Bank Menu =====")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            if account:
                deposit()
            else:
                print("Create account first!\n")
        elif choice == '3':
            if account:
                withdraw()
            else:
                print("Create account first!\n")
        elif choice == '4':
            if account:
                check_balance()
            else:
                print("Create account first!\n")
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice!\n")


# Run program
main()

 #Mini Project 8: Voting System
 # Voting System

votes = {
    "Alice": 0,
    "Bob": 0,
    "Charlie": 0
}

# Add vote
def add_vote():
    name = input("Enter candidate name: ")

    if name in votes:
        votes[name] += 1
        print("Vote added successfully!\n")
    else:
        print("Candidate not found!\n")


# Display results
def display_results():
    print("\n--- Voting Results ---")
    for candidate, count in votes.items():
        print(f"{candidate} : {count} votes")

    # Find winner
    winner = max(votes, key=votes.get)
    print(f"\nWinner: {winner}")
    print("----------------------\n")


# Main loop
def main():
    while True:
        print("===== Voting Menu =====")
        print("1. Add Vote")
        print("2. Show Results")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_vote()
        elif choice == '2':
            display_results()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice!\n")


# Run program
main()

#Mini Project 9: Course Enrollment System
# Course Enrollment System

students = []

# Add student
def add_student():
    name = input("Enter student name: ")
    courses = input("Enter courses (comma separated): ").split(",")

    student = {
        "name": name,
        "courses": [c.strip() for c in courses]
    }

    students.append(student)
    print("Student added successfully!\n")


# Update courses
def update_courses():
    name = input("Enter student name to update: ")

    for student in students:
        if student["name"] == name:
            courses = input("Enter new courses (comma separated): ").split(",")
            student["courses"] = [c.strip() for c in courses]
            print("Courses updated successfully!\n")
            return

    print("Student not found!\n")


# Display students
def display_students():
    if not students:
        print("No students found.\n")
        return

    print("\n--- Student Details ---")
    for student in students:
        print(f"Name: {student['name']}")
        print(f"Courses: {', '.join(student['courses'])}")
        print("----------------------")
    print()


# Main menu
def main():
    while True:
        print("===== Course Enrollment Menu =====")
        print("1. Add Student")
        print("2. Update Courses")
        print("3. Display Students")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            update_courses()
        elif choice == '3':
            display_students()
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice!\n")


# Run program
main()

#Mini Project 10: Number Utility Tool
# Number Utility Tool

# Function to convert number
def convert_number(num):
    print("\n--- Number Conversions ---")
    print(f"Binary      : {bin(num)}")
    print(f"Octal       : {oct(num)}")
    print(f"Hexadecimal : {hex(num)}")


# Function to format number
def format_number(num):
    print("\n--- Number Formatting ---")
    print(f"With commas        : {num:,}")
    print(f"Scientific notation: {num:.2e}")


# Main function
def main():
    num = int(input("Enter a number: "))

    convert_number(num)
    format_number(num)


# Run program
main()
