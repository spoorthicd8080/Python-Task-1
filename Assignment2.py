#Bitwise Operator Tasks
#1. 
a = 10
b = 6

result = a & b

print(result)

#2.
x = 12
y = 5

result = x | y

print(result)

#3.
num = 8

result = ~num

print(result)

#4.
a = 15
b = 9

result = a ^ b

print(result)

#5.
num = 7

result = num << 2

print(result)

#6
num = 20

result = num >> 1

print(result)

#7
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = a & b

print("AND result:", result)

#8.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = a ^ b

print("XOR result:", result)

#String Tasks
#9.
text = "hi"

result = text * 4

print(result)

#10.
text = "python"

print(text * 3)

#11.
str1 = "super"
str2 = "man"

result = str1 + str2

print(result)

#12.
str1 = "hello"
str2 = " "
str3 = "world"

print(str1 + str2 + str3)

#13.
name = input("Enter your name: ")

print(name * 5)

#14.
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

result = str1 + str2

print("Concatenated string:", result)

#Input and Casting Tasks
#15.
name = input("Enter your name: ")

print(type(name))

#16.
age = int(input("Enter your age: "))

print(age)

#17.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2

print("Sum:", sum)

#18.
mark1 = float(input("Enter first mark: "))
mark2 = float(input("Enter second mark: "))

average = (mark1 + mark2) / 2

print("Average:", average)

#19.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = 3 * a * 2 + b - 2

print("Result:", result)

#20.
num = input("Enter a number: ")

print("Before type casting:", type(num))

num = int(num)

print("After type casting:", type(num))

#Unit Digit Tasks
#21.
num = input("Enter a number: ")

print("Last digit:", num[-1])

#22.
num = int(input("Enter a number: "))

unit_digit = num % 10

print("Unit digit:", unit_digit)

#23.
num = int(input("Enter a number: "))

result = num // 10

print("Number after removing last digit:", result)

#24.
num = int(input("Enter a number: "))

second_last = (num // 10) % 10

print("Second last digit:", second_last)

#25.
num = int(input("Enter a 5 digit number: "))

last_digit = num % 10

print("Last digit:", last_digit)

#IF Statements Tasks
#26.
if 10 >= 5:
    print("10 is greater than or equal to 5")
else:
    print("Condition is false")
    
#27.
num = int(input("Enter a number: "))

if num > 50:
    print("The number is greater than 50")
else:
    print("The number is not greater than 50")
    
#28.
age = int(input("Enter your age: "))

if age >= 18:
    print("Age is greater than or equal to 18")
else:
    print("Age is less than 18")

#29.
num = int(input("Enter a number: "))

if num > 100:
    print("The number is greater than 100")
else:
    print("The number is not greater than 100")
    
#30.
num = int(input("Enter a number: "))

if num >= 0:
    print("The number is greater than or equal to 0")
else:
    print("The number is less than 0")

#IF Else Tasks
#31.
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
    
#32.
marks = int(input("Enter your marks: "))

if marks >= 35:
    print("Pass")
else:
    print("Fail")
    
#33.
num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
else:
    print("Negative number")

#34.
num = int(input("Enter a number: "))

if num > 10:
    print("The number is greater than 10")
else:
    print("The number is not greater than 10")

#Nested If Tasks
#35.
age = int(input("Enter age: "))
height = int(input("Enter height (cm): "))
weight = int(input("Enter weight (kg): "))

if age >= 18 and height >= 160 and weight >= 60:
    print("Selected")
else:
    print("Rejected")
    
#36.
marks = int(input("Enter marks: "))
age = int(input("Enter age: "))

if marks >= 60 and age >= 17:
    print("Admission Granted")
else:
    print("Admission Denied")
    
#37.
age = int(input("Enter age: "))
height = int(input("Enter height (cm): "))
weight = int(input("Enter weight (kg): "))

if age >= 16 and height >= 150 and weight >= 50:
    print("Selected")
else:
    print("Not Selected")

#Match Statememt Tasks     
#38.
day = int(input("Enter a number (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid number")
        
#39.
num = int(input("Enter a number (1-3): "))

match num:
    case 1:
        print("Red")
    case 2:
        print("Blue")
    case 3:
        print("Green")
    case _:
        print("Invalid number")
        
#40.
num = int(input("Enter a number (1-4): "))

match num:
    case 1:
        print("Apple")
    case 2:
        print("Mango")
    case 3:
        print("Orange")
    case 4:
        print("Banana")
    case _:
        print("Invalid number")
                                  
  