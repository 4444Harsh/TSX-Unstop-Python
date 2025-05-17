# Tasks:
# 1. Write a script to calculate the area and perimeter of a rectangle
# using variables.
# 2. Write a script that takes two numbers as input and prints whether
# the first number is greater than, less than, or equal to the second
# number. 1

# 3. Write a script that checks if a given year is a leap year (divisible by
# 4, but not by 100 unless also divisible by 400).
# 4. Experiment with different arithmetic and logical operators in the
# interpreter.
# 5. Write a script that concatenates two strings and prints the result. 
#############################
#solution 1.->
def area(a,b):
  return a*b
def perimeter(a,b):
  return 2*(a+b)
##########################################
# solution 2.->
#: Compare Two Numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print("The first number is greater than the second.")
elif num1 < num2:
    print("The first number is less than the second.")
else:
    print("Both numbers are equal.")

# solution 3: Check if a Year is a Leap Year
year = int(input("\nEnter a year to check if it's a leap year: "))

if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# solution 4: Experimenting with Arithmetic and Logical Operators
print("\nArithmetic and Logical Operators Examples:")
a, b = 10, 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")

print(f"{a} > {b} and {a} != {b} => {a > b and a != b}")
print(f"{a} < {b} or {a} == 10 => {a < b or a == 10}")
print(f"not ({a} == {b}) => {not (a == b)}")

# solution 5: Concatenate Two Strings
str1 = input("\nEnter first string: ")
str2 = input("Enter second string: ")

concatenated = str1 + str2
print("Concatenated string:", concatenated)
