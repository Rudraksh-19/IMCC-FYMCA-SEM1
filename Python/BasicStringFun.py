# Initial text assignment
text = "welcome to IMCC"

# removes leading and trailing whitespace
print("Remove space", text.strip())

# converts all characters to uppercase 
print("Uppercase", text.upper())

# converts all characters to lowercase 
print("Lowercase", text.lower())

# Explicitly reassign the stripped text
text = text.strip()

# converts only the very first character of the string to uppercase 
print("Capitalize first letter : ", text.capitalize())

# capitalizes the first character of each word 
print(text.title())

# returns the number of non-overlapping occurrences of the substring 
print("Letter C Occurs", text.count("C"), "times in text")

# returns the lowest index where the substring starts 
print("Position of IMCC in text is", text.find("IMCC"))

# replace(old, new) returns a copy with all occurrences of "IMCC" replaced by "Python Magic"
print(text.replace("IMCC", "Python Magic"))

# checks if the string begins with " We" (returns False; string begins with "welcome")
print(text.startswith(" We"))

# checks if the string ends with "!  " (returns False; string ends with "IMCC")
print(text.endswith("!  "))

# splits the string on whitespace into a list of words
print("Simple split", text.split())

# Define a list of strings
words = ["Python", "Is", "Fun"]

# concatenates elements of an iterable using the specified delimiter 
print(" ".join(words))