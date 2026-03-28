#Task 1:User Info Manager (Functions + Dictionary)

# Function to create a user
def create_user(name, age, role):
    return {
        "name": name.title(),  # Format name using .title()
        "age": age,
        "role": role
    }

# List to store multiple users
users = []

# Adding users
users.append(create_user("john doe", 25, "developer"))
users.append(create_user("jane smith", 30, "designer"))
users.append(create_user("alice johnson", 28, "manager"))

# Print all users
for user in users:
    print(user)
    
 #Task 2: Dynamic Calculator (*args)
    
# Function to calculate total and average
def calculate_total(*numbers):
    total = sum(numbers)
    
    if len(numbers) == 0:
        average = 0
    else:
        average = total / len(numbers)
    
    return total, average


# Example usage
result = calculate_total(10, 20, 30, 40)

# Unpacking results
total, average = result

print("Total:", total)
print("Average:", average)    

#Task 3: Keyword Config System (**kwargs)
# Function to handle system configuration
def system_config(**settings):
    for key, value in settings.items():
        print(f"{key}: {value}")

# Example usage
system_config(mode="debug", version="1.0", theme="dark")

#Task 4: Factorial Service (Recursion)

# Recursive factorial function
def factorial(n):
    if n < 0:
        return "Error: Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Example usage
print("Factorial of 5:", factorial(5))
print("Factorial of 0:", factorial(0))
print("Factorial of -3:", factorial(-3))

#Task 5: Memory Optimization (Generator)

# Generator function (yields squares one by one)
def square_generator(n):
    for i in range(1, n + 1):
        yield i * i


# Normal list approach (stores all values in memory)
def square_list(n):
    return [i * i for i in range(1, n + 1)]


# Example usage
n = 5

squares_list = square_list(n)
squares_gen = square_generator(n)

print("List result:", squares_list)
print("Type of list:", type(squares_list))

print("\nGenerator object:", squares_gen)
print("Type of generator:", type(squares_gen))

print("\nSquares from generator:")
for value in squares_gen:
    print(value)
    
#Task 6: Exception Handling Module

try:
    # Taking input from user
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    # Division operation
    result = numerator / denominator
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input! Please enter integers only")

finally:
    print("Program Completed")
    
#Task 7: File Handling

# Writing user details into file
file = open("team_data.txt", "w")

file.write("Name: John Doe, Age: 25, Role: Developer\n")
file.write("Name: Jane Smith, Age: 30, Role: Designer\n")
file.write("Name: Alice Johnson, Age: 28, Role: Manager\n")

# Bonus: check if file is closed
print("Is file closed after writing?", file.closed)

file.close()

print("Is file closed after close()?", file.closed)


# Reading file content
file = open("team_data.txt", "r")
content = file.read()

print("\n--- File Content ---")
print(content)

file.close()