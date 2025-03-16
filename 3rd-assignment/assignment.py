# Control Flow & Loops
# If Else Statement
age = 18;
if age >= 18:
    print("You are an adult");
else:
    print("You are not an adult");

#  for loop
for i in range(1, 10):
    print(f"Iteration {i}"); # prints 1 to 9

# while loop
count = 0;
while count < 5:
    print(f"Count is {count}");
    count += 1; # prints 1 to 9

# Lists, Tuples & Dictionary
# List
fruits = ["Apple", "Banana", "Cherry"]
fruits.append("Mango")  # Add an element
print(fruits[1])  # Accessing elements
print(fruits)  # Print the whole list
fruits.remove("Banana")  # Remove an element
print(fruits)  # Print the whole list

# Tuple
colors = ("Red", "Green", "Blue")
print(colors[1])  # Accessing elements
print(colors)  # Print the whole tuple

# Dictionary
student = {
    "name": "John",
    "age": 18,
    "course": "Computer Science"
}
print(student["name"])  # Accessing elements  # John
student["age"] = 19  # Updating an element
print(student)  # Print the whole dictionary  # {'name': 'John', 'age': 18, 'course': 'Computer Science'}


# The Set & Frozenset
# Set (unordered collection of unique elements or mutable)
fruits = {"Apple", "Banana", "Cherry"}  # Create a set
fruits.add("Mango")  # Add an element
print(fruits)  # Print the whole set
fruits.remove("Banana")  # Remove an element
print(fruits)  # Print the whole set

# Frozenset (immutable set)
immutable_set = frozenset([1, 2, 3, 4, 5])  # Create a frozenset
#immutable_set.add(6)  # AttributeError: 'frozenset' object has no attribute 'add'
print(immutable_set)  # Print the whole frozenset


