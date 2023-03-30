from collections import namedtuple

# Define the Person named tuple
Person = namedtuple('Person', ['name', 'age', 'city'])

# Create an array of Person objects
people = [
    Person('Alice', 25, 'New York'),
    Person('Bob', 30, 'San Francisco'),
    Person('Charlie', 35, 'Chicago'),
    Person('David', 40, 'Los Angeles'),
    Person('Eve', 45, 'Boston')
]

# Calculate the number of rows and columns needed
num_rows = (len(people) + 2) // 3
num_cols = 3

# Print the array in rows and columns
for i in range(num_rows):
    for j in range(num_cols):
        index = i*num_cols + j
        if index < len(people):
            person = people[index]
            print(f"{person.name.ljust(10)} {person.age:<5} {person.city}")
    print()
