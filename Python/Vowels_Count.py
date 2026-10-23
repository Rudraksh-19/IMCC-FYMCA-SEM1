sentence = input("Enter your string : ")
vowels = "aeiouAEIOU"
count = 0

for char in sentence:
    if char in vowels:
        count += 1  
print("Total vowels:", count)