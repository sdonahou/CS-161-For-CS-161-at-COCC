#1 A function that creates a new string based on the first.
phrase = input("Enter a phrase : ")
uppercase_phrase = input("Enter the same phrase but in upper case : ")
if phrase.upper() == uppercase_phrase:
    print('Stop shouting!"')

#2 A function that uses the in command to see if a character is found in a string.
user_input = input("Enter a string : ")
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0

for vowel in vowels:
    if vowel in user_input:
        vowel_count += 1
print(f"{user_input} has {vowel_count} different vowels")

#3 Program that identifies greater than placement in a string
user_input_1 = input("Enter a string : ")
user_input_2 = input("Enter another string : ")

if user_input_1 < user_input_2:
    print(f"{user_input_1} comes before {user_input_2}")
else:
    print(f"{user_input_2} comes after {user_input_1}")

#4 Function to check matching email addresses.
email1 = input("Enter your email : ")
email2 = input("Enter your email : ")
if email1 == email2:
    print("Thank you")
else: print("The two inputs did not match. Please try again")

