# 1. print sum of first 10 even numbers
total = sum(range(2, 22, 2))
print("Sum of first 10 even numbers:", total)

# 2. accept two values S and N. print square of firt N numbers starting from s
S = int(input("Enter starting value (S): "))
N = int(input("Enter number of terms (N): "))
print(f"\nSquares of the first {N} numbers starting from {S}:")
for num in range(S, S + N):
    print(f"{num}^2 = {num ** 2}")

# 3. Reverse the accepted string
text = input("Enter a string: ")
reversed_text = text[::-1]
print("Reversed string:", reversed_text)

# 4. Accept sentence from user and count the vowels
sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = 0
for char in sentence:
    if char in vowels:
        count += 1
print("Number of vowels:", count)

# 5. Remove duplicates from list
original_list = [10, 20, 10, 30, 40, 20, 50, 30]
unique_list = list(dict.fromkeys(original_list))
print("Original list:", original_list)
print("List without duplicates:", unique_list)

# 6. Reverse the list
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print("Reversed list:", reversed_list)