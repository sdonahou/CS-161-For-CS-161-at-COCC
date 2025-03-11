# 1 For loop that prints all even numbers between two numbers that's input.
first = int(input("Enter low number: "))
second = int(input("Enter high number: "))

print("The even numbers between", first, "and", second, "are")

for num in range(first, second + 1):
    if num % 2 == 0:
        print(num)

#2 A while loop that points out factors of a given positive integer.
integer = int(input("Enter a positive integer: "))
print("The integers that are factors of", integer, "are: ")

factor = 1

while factor <= integer:
    if integer % factor == 0:
        print(factor)
    factor += 1

# 3 An iteration program that calculates the sum of a numeric position of letters of a last name.
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "I", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
name = input("Enter a name: ")
total = 0
for letter in name:
    if letter in alphabet:
        total += alphabet.index(letter)
print("The sum of the numeric position is: ", total)

# 4 Recursive function that takes one positive integer as a parameter
def numsquared(number):
    if number == 1:
        print(1)
    else:
        numsquared(number - 1)
        print(number * number)
number = int(input("Enter a positive integer: "))
numsquared(number)


