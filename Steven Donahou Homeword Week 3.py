
# 1) Function that asks the user to enter their name.
x = input("What is your name?: ")

print("Hello, " + x + ",")

# 2) Function that asks the user to enter their age
#First attempt produced an error "TypeError: can only concatenate str (not "int") to str"
#After adding the str() function around the number the predicted age allowed for a UTF-8 representation.
x= input("What is your age?: ")
x= int(x)
predicted_age = x + 5

print (str(predicted_age))

# 3) Function that uses concatenation and str() to print a message forcasting the users age in y years.
x= input("What is your age?: ")
x= int(x)
predicted_age = x + 5


print("In 5 years you will be " + str(predicted_age) + " years old.")

#4) Function to ask the user to enter a value that might be a floating point.
weekly_hours = float(input("Enter the hours you have worked this week: "))
hourly_wage = float(input("Enter your hourly wage, without th $ sign: "))

#5) Function to calculate the users hourly and annual wage from the information given of #4.
print("Your gross pay this week is: $", hourly_wage * weekly_hours)
print("Your annual gross pay will be: $", hourly_wage * weekly_hours * 52.14  )
