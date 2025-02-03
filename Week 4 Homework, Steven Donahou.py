#1 Define a function that returns the average of 3 numbers.
def average(num1, num2, num3):
    return(num1 + num2 + num3) / 3

print(average(7, 5, 9))
print(average(6, 6, 7))

#2 Move the function definition after the print statements.
#The script runs only because it's defined from above.
#Without the definition from above it gives an error name 'average' is not defined.
print(average(7, 5, 9))
print(average(6, 6, 7))

def average(num1, num2, num3):
    return(num1 + num2 + num3) / 3

#3 Print out the value of a parameter outside of a function definition.
#3 This gives an error since num1 corresponds with its average() definition.
def average(num1, num2, num3):
    return(num1 + num2 + num3) / 3

print(average(7, 5, 9))
print(average(6, 6, 7))
#print(num1)

#4 Define a function that converts a dog's age into human years.
def dog_age_in_human_years(dogs_age):
    return 24 + (dogs_age - 2) * 4
dogs_age = int(input("Dogs age: "))
print(dogs_age, "dog years is equivalent to", dog_age_in_human_years(dogs_age), "human years. ")

#5 Define a function that'll calculate the value of a car using an input function that includes the price, number of years, and car type.
def car_value(price, years, type):
    if type == "German":
        rate = 1 - (.05 * years)
    elif type == "Japanese":
        rate = 1 - (.07 * years)
    elif type == "Italian":
        rate = 1 + (.05 * years)
    value = price * (rate ** years)
    return "The value of the " + type + " car will be $ " + str(round(value, 2)) + " after " + str(years) + " years. "


price = float(input("Price: "))
years = int(input("Years: "))
type = input("Car types (German, Japanese, Italian): ")

print(car_value(price, years, type))

#6 Define a function that converts a dogs age into human years and returns the result
def dog_age_in_human_years(dogs_age):
    return 24 + (dogs_age - 2) * 4
dogs_age = int(input("Dogs age: "))
name = input("What is your dogs name? ")
print(dog_age_in_human_years(dogs_age))
print("Your " + name + " is ",dog_age_in_human_years(dogs_age) , "human years old. ")