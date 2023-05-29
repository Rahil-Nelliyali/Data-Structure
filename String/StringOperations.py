# Concatenation
string1 = "Hello"
string2 = "World"
concatenated_string = string1 + " " + string2
print(concatenated_string)  # Output: Hello World

# Length
length = len(concatenated_string)
print(length)  # Output: 11

# Accessing characters
first_char = concatenated_string[0]
last_char = concatenated_string[-1]

print(first_char)  # Output: H
print(last_char)  # Output: d

# Slicing
substring = concatenated_string[6:11]
print(substring)  # Output: World

# Changing case
lowercase = concatenated_string.lower()
uppercase = concatenated_string.upper()
print(lowercase)  # Output: hello world
print(uppercase)  # Output: HELLO WORLD

# Searching
index = concatenated_string.index("World")
print(index)  # Output: 6

# Counting occurrences
count = concatenated_string.count("l")
print(count)  # Output: 3

# Replacing
replaced_string = concatenated_string.replace("Hello", "Hi")
print(replaced_string)  # Output: Hi World

# Splitting
words = concatenated_string.split()
print(words)  # Output: ['Hello', 'World']

# Joining
joined_string = "-".join(words)
print(joined_string)  # Output: Hello-World


# Reverse a string using slicing
def reverse_string(string):
    return string[::-1]

# Example usage:
# original_string = "Hello, World!"
# reversed_string = reverse_string(original_string)
# print(reversed_string)
