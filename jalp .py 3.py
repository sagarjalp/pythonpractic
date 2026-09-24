#  Convert a float 7.9 into an integer and print both the value and its type.
x = 7.9
print(type(x))
result = int(x)
print(result)
print(type(result))

# Write a program that takes a string "123" and converts it into an integer, then adds 10.
x = "123"
print(x)
result = int(x) + 10
print(type(result))
print(result)

# Print a string that contains both single and double quotes using escape characters.


# Concatenate two strings "Python" and "Rocks" with a space in between.
num1 = "python"
num2 = "rocks"
result = num1 + " " + num2
print(result)

# Repeat the string "Hi! " five times.
x = "hi"
result = "hi" * 5
print(result)

# Slice the string "Programming" to get "gram".
x = "programming"
result = x[3:7]
print(result)

# Use negative indexing to print the last 3 characters of "HelloWorld".
x = "HelloWord"
result = x[-3:]
print(result)

# Write a program that:

# a.Takes the string " I love Python programming! "
x = " I love python programing! "
print(x)

# b. Strips whitespace
x = " I love python programing! "
result = x.strip()
print(result)

# Converts it to uppercase
x = "I love python programing!"
result = x.upper()       
print(result)
# d. Replaces "Python" with "Java"
x = "I love python programing!"
result = x.replace("python", "java")
print(result)

# e. Splits it into words
x = "I love python programing!"
result = x.split()
print(result)

