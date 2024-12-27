
#List Comprehensions:
squares = [x**2 for x in range(10)]  # Creates a list of squares [0, 1, 4, 9, ..., 81]


#Enumerate for Indexed Loops:
for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)

#F-strings for Formatting:
name = "Alice"
age = 30
print(f"My name is {name}, and I'm {age} years old.")

#Unpacking with *:
a, *b, c = [1, 2, 3, 4, 5]
print(a, b, c)  # Output: 1 [2, 3, 4] 5

#Use zip() for Parallel Iteration:
for a, b in zip([1, 2, 3], ['a', 'b', 'c']):
    print(a, b)  # Output: (1, 'a'), (2, 'b'), (3, 'c')
