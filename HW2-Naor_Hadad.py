# A
X = int(input("enter a number for X :"))
Y = int(input("enter a number for Y :"))

if X > Y:
    print(f"X is bigger then Y {X} > {Y} ")
elif X < Y:
    print(f"X is Smaller then Y {X} < {Y} ")
else:
    print(f"X is equal to Y {X} = {Y}")

# B
for i in range(1, 6):
    print(f"{i}.")

# C
X2 = int(input("enter a number from 1 to 4:"))
X_out_of_range = X2 > 4 or X2 < 1
X_equal_one = 1
X_equal_two = 2
X_equal_tree = 3
X_equal_four = 4
if X_out_of_range:
    print("The number you selected is out of range ")
elif X2 == X_equal_one:
    print(f"{X_equal_one} = Summer")
elif X2 == X_equal_two:
    print(f"{X_equal_two} = Winter")
elif X2 == X_equal_tree:
    print(f"{X_equal_tree} = Fall")
else:
    print(f"{X_equal_four} = Spring")

# D - it will run until count will be equl 10 and it's starting from 1 so it will run 10 times
# E-

age = 32
first_letter_of_last_name = "H"
current_sekel_vs_dollar_currency = 3.61
flew_abroad = True
apartment_number = 18

print(f"my age is {age} and the first letter of my last name is {first_letter_of_last_name}"
      f"the current sekel value against the dolar value is {current_sekel_vs_dollar_currency}"
      f"I did flew abroad this year {flew_abroad} and my apartment number is {apartment_number}")

age_and_currency_sum = age + current_sekel_vs_dollar_currency

print(f"sum of age + currency value = {age_and_currency_sum}")

# F

user_phone_number = int(input("please enter your phone number : "))
print(f"your phone number is : {user_phone_number}")


def printHello():
    print("Hello")


printHello()


def calculate(a=5, b=3.2):
    result = a + b
    print(result)
    return (result)


calculate(5, 3.2)

# H
def WhatIsYourName() :
    name = input("please enter your name :")
    print(name)
    return(name)

WhatIsYourName()

def Number_div_by_two() :
    Number = int(input("please enter a number :"))
    number_div = Number/2
    print(f"{Number}/2 = {number_div}")
    return(number_div)

Number_div_by_two()

# I

def addition():
    first_number = int(input("enter first number :"))
    second_number = int(input("enter second number :"))
    sum = first_number + second_number
    print(f"the sum of {first_number} + {second_number} is {sum}")
    return sum

addition()

def addString() :
    first_str = input("please enter first string :")
    second_string = input("please enter second string :")
    add_string_with_space = (f"{first_str} {second_string}")
    print(add_string_with_space)
    return add_string_with_space

addString()

# K
height = 5

for i in range(height):
    for j in range(i+1):
        print("#", end="")
    print()

# L
size = 7

for i in range(size):
    for j in range(size):
        # Print "#" if the index of row equals the index of column or
        # the index of row and column are symmetrical around the center
        if i == j or i + j == size - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()

# M
def get_number_from_user():
    number = input("Please enter a number: ")
    return int(number)

def compute_sum_of_digits(number):
    sum_of_digits = sum(int(digit) for digit in str(number))
    return sum_of_digits

user_number = get_number_from_user()
sum_of_digits = compute_sum_of_digits(user_number)
print(f"The sum of the digits in {user_number} is {sum_of_digits}.")









