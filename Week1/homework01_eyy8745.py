""""
#1
word = input("Enter a word: ").lower()
vowels = "aeiou"
count = 0
for i in word:
    if i in vowels:
        count += 1
print("Number of vowels: " + count)

#2
animals=['tiger', 'elephant', 'monkey', 'zebra', 'panther']
for i in animals:
    print(i.upper())

#3
for i in range(1,21):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")

#4
word = input("Enter a string: ")
if word == word[::-1]:
    print("Your string is a palindrome")
else:
    print("Your string is not a palindrome")

#5
def sum_of_integers(a, b):
    return a + b
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
print("The sum is:", sum_of_integers(a,b))
"""
