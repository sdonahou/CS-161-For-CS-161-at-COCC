#1 Make a while statement that.
x = int(input("Enter an integer: "))

while x > 0:
    print(x)
    x = x - 1

print("blastoff!!")

#2 Function that determines if an integer is odd or even.
x = int(input("Enter an integer: "))

while x > 0:
    if x % 2 == 0:
        print(x, "is an even number.")
    else:
        print(x, "is an odd number.")
    x = x - 1
print("blastoff!!")

#3 Function that determines a decrease in value.
x = int(input("Enter an integer: "))

decrease = int(input("Enter a decreasing number: "))

while x > 0:
    if x % 2 == 0:
        print(x, "is an even number.")
    else:
        print(x, "is an odd number.")
    x -= decrease
    print("blastoff!!")

#4 A loop that prints out "goodbye" if a word is less than 5.
while True:
    word = input("Enter a word: ")
    if len(word) < 5:
        print("goodbye")
        break
    print(word, "has", len(word), "letters.")

#5 A while loop that counts from 10 to 100 in decimal, binary, and hex
x = 10

while x <= 100:
    print(x, bin (x), hex(x))
    x = x + 1

#6 Two functions that print number of stars that are equal to the parameter (5)
def squarex_iteration(stars):
  for star in range(stars, 0, -1):
      print("*" * star)
squarex_iteration(5)

def square_recursive(stars):
    if stars > 0:
        print("*" * stars)
        square_recursive(stars - 1)
square_recursive(5)