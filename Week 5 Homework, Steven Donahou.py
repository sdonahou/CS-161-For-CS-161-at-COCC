# 1)Determine with an if statement a number that is divisible by 5.
num =(float(input("Enter a number: ")))

if num % 5 == 0:
    print( num, "is divisible by 5 ")

# For when a number is not divisible
else:
    print(num, "is not divisible by 5")

# 2) Use if and elifs to determine a state capital
state = input("Enter a U.S state: ")

if(state == "Oregon"):
    print("Salem.")

elif(state == "Washington"):
    print("Olympia.")

elif(state == "California"):
    print("Sacramento.")

elif(state == "Colorado"):
    print("Denver.")

elif(state == "New Mexico"):
    print("Santa Fe.")

elif(state == "Illinois"):
    print("Springfield.")

#For when a capital is not known
else:
    print("sorry, I do not know that one.")

# 2.1) Create a dictionary for known state capitals using .get()
stateCapitals = {
    "Oregon": "Salem",
    "Washington": "Olympia",
    "California": "Sacramento",
    "Colorado": "Denver",
    "New Mexico": "Santa Fe.",
    "Illinois": "Springfield",
}
#For when a capital is not provided within the provided dictionary.
state = input("Enter a U.S state: ")
capital = stateCapitals.get( state, "sorry, I don't know that one.")
print(capital)

#3 Use the match case to find the capital
state = input("Enter a U.S state: ")

match state:
    case "New Mexico":
      print("Santa Fe.")
    case "Oregon":
      print("Salem.")
    case "Washington":
        print("Olympia.")
    case "California":
        print("Sacramento.")
    case "Colorado":
        print("Denver.")
    case "Illinois":
        print("Springfield.")
    case _:
        print("sorry, I do not know that one.")

#4 Using elif in a function as well as docstrings to document.
'''
Function that provides an entrance to a public pool according to age

if under 2 years, $0
Age 2-12, $3
Age 12-60, $6
Above 60 years, $4 


'''
def pool_admission(age):
    if (age < 2):
        return 0
    elif (age < 12):
        return 3
    elif (age <= 60 ):
        return 6
    else:
        return 4
age = int(input("Enter you age for admission:"))
print("$",pool_admission(age),"Admission price")

#4 Determine how many times the string 160 appears in HTML for coccbobcat.com
import requests

url = 'http://coccbobcat.com./'
response = requests.get('http://coccbobcat.com./')
response.raise_for_status()
html_content = response.text
substring = "160"
count= html_content.count(substring)

print("The substring ",substring, "appears ",count, "times of ",url, ".")

#Program that determines the number of process running on system
import psutil

def processes():
    return len(psutil.pids())
num_processes = processes()
print("Number of running processes", num_processes)


