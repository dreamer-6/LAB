numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

students = [
    {"name": "John", "age": 20, "grade": 75},
    {"name": "rose", "age": 22, "grade": 90},
    {"name": "jack", "age": 20, "grade": 92},
    {"name": "David", "age": 23, "grade": 50}
]

fruits = ["Apple", "banana", "cherry", "date", "elderberry"]

# Map operations
squares = list(map(lambda x: x**2, numbers))
student_names = list(map(lambda x: x["name"], students))
uppercase_fruits = list(map(lambda x: x.upper(), fruits))

# Filter operations
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
top_students = list(filter(lambda x: x["grade"] > 85, students))

# Case-insensitive check for the letter 'A'
fruits_with_a = list(filter(lambda x: 'a' in x.lower(), fruits))

# List modifications
numbers.reverse()
# You can combine sort and reverse into a single step!
students.sort(key=lambda x: x["age"], reverse=True)

# Print statements
print("Squares:", squares)
print("Student Names:", student_names)
print("Uppercase Fruits:", uppercase_fruits)
print("Even Numbers:", even_numbers)
print("Top Students:", top_students)
print("Fruits with A:", fruits_with_a)
print("Reversed Numbers:", numbers)
print("Sorted Students (by Age Descending):", students)