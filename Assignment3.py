#  Loop Basics
#1.
for i in range(1, 51):
    print(i)
    
#2.
for i in range(2, 101, 2):
    print(i)

#3.
for i in range(1, 101, 2):
    print(i)
    
#4.
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")
    
#5.
total = 0
for i in range(1, 101):
    total += i

print("Sum =", total)

#6.
for i in range(50, 0, -1):
    print(i)
    
#7.
count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count += 1

print("Count =", count)

#8.
for i in range(1, 11):
    print(i, "->", i * i)
    
#9.
for i in range(1, 11):
    print(i, "->", i * i * i)
    
#10.
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(i)
    
#While Loop
#11.
i = 1

while i <= 20:
    print(i)
    i += 1

#12.
n = int(input("Enter a number: "))

fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print("Factorial =", fact)

#13.
n = int(input("Enter a number: "))

reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

print("Reversed number =", reverse)

#14.
n = int(input("Enter a number: "))

count = 0

while n > 0:
    n //= 10
    count += 1

print("Number of digits =", count)

#15.
user_input = ""

while user_input.lower() != "stop":
    user_input = input("Enter something (type 'stop' to end): ")
    
    if user_input.lower() != "stop":
        print("You entered:", user_input)
        
#Nested Loop    
#16.
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()
    
#17.
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()

#18.
for i in range(1, 6):       
    print("Table of", i)
    
    for j in range(1, 11):  
        print(i, "x", j, "=", i * j)
    
    print()  

#19.
for i in range(3):          # 3 rows
    for j in range(3):      # 3 columns
        print(chr(65 + j), end=" ")
    print()    
    
#20.
num = 1

for i in range(3):        # 3 rows
    for j in range(3):    # 3 columns
        print(num, end=" ")
        num += 1
    print()
    
# String Basics
#21.
text = input("Enter a string: ")

count = len(text)

print("Total characters =", count)

#22.
text = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)

print("Number of vowels =", count)

#23.
text = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = sum(1 for char in text if char.isalpha() and char not in vowels)

print("Number of consonants =", count)

#24.
text = input("Enter a string: ")

reverse = ""

for char in text:
    reverse = char + reverse

print("Reversed string =", reverse)

#25.
text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#String Slicing    
#26.text = input("Enter a string: ")

print("First 5 characters:", text[:5])

#27.
text = input("Enter a string: ")

print("Last 3 characters:", text[-3:])

#28.
text = input("Enter a string: ")

reverse = text[::-1]

print("Reversed string =", reverse)

#29.
text = input("Enter a string: ")

print("Every 2nd character:", text[::2])

#30.
text = input("Enter a string: ")

result = text[1:-1]

print("Result:", result)

#List Basics
#31.
numbers = [10, 20, 30, 40, 50]

total = sum(numbers)

print("Sum =", total)

#32.
numbers = [10, 25, 5, 40, 15]

max_value = max(numbers)

print("Maximum value =", max_value) 

#33.
numbers = [10, 25, 5, 40, 15]

min_value = min(numbers)

print("Minimum value =", min_value)

#34.
numbers = [10, 20, 30, 40, 50]

count = len(numbers)

print("Total elements =", count) 

#35.
numbers = [10, 20, 30, 40, 50]

element = int(input("Enter element to search: "))

if element in numbers:
    print("Element found")
else:
    print("Element not found")
    
#List Operations
#36.
numbers = []

numbers.append(10)
numbers.append(20)
numbers.append(30)

print("List:", numbers)

#37.
numbers = [10, 20, 30, 40]

numbers.insert(2, 25)   # Insert 25 at index 2

print("Updated list:", numbers)

#38.
numbers = [10, 20, 30, 40, 50]

numbers.remove(30)   # Removes element 30

print("Updated list:", numbers)

#39.
numbers = [10, 20, 30, 40, 50]

reversed_list = []

for num in numbers:
    reversed_list.insert(0, num)   # Insert at beginning

print("Reversed list:", reversed_list)

#40.
numbers = [50, 20, 40, 10, 30]

n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            # swap
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)
