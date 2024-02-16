# Khan_Shahmeer 201662879 October 2022 CA-03.py
# Calculating and converting the age of cats into human years 

# Input and main menu section
import sys

print("\tCat Age Main Menu")
print("---------------------------")
print("A. Months 8 to 24")
print("B. Years 3 to 6")
print("X. Exit Program")
option = input("\nEnter options A, B, or X: ")

# Validation section that checks if the user inputs an option within the range otherwise the program will end
# prematurely
input_flag = 0
while not input_flag:
        if option == 'A' or option == 'a' or option == 'B' or option == 'b' or option == 'X' or option == 'x':
                input_flag = 1
        else:
            print(option,"is not a valid option")
            break

# Section of code outputs the life stage of the cat and calculates the age in human years (Option A)
if input_flag == 1:
  if option == 'A' or option == 'a':
    age_Months = input("Please enter the age of your cat in months: ")

    if age_Months == '8':
        print("The cat is in the junior stage")
        print("The cat is 11 years old in human years")

    elif age_Months == '12':
        print("The cat is in the junior stage")
        print("The cat is 15 years old in human years")

    elif age_Months == '18':
        print("The cat is in the junior stage")
        print("The cat is 21 years old in human years")

    elif age_Months == '24':
        print("The cat is in the junior stage")
        print("The cat is 27 years old in human years")

    else:
        print("Age entered is outside of the range")
    sys.exit()

# Section of code outputs the life stage of the cat and calculates the age in human years (Option B)
if option == 'B' or option == 'b':
    age_Years = input("Please enter the age of your cats in years: ")

    if age_Years == '3':
        print("The cat is in the prime stage")
        print("The cat is 28 years old in human years")

    elif age_Years == '4':
        print("The cat is in the prime stage")
        print("The cat is 32 years old in human years")

    elif age_Years == '5':
        print("The cat is in the prime stage")
        print("The cat is 36 years old in human years")

    elif age_Years == '6':
        print("The cat is in the prime stage")
        print("The cat is 40 years old in human years")

    else:
        print("Age entered is outside of the range")
    sys.exit()  # Exits the program once the selection statements have finished in order to prevent traceback errors

# Program exit section
if option == 'X' or option == 'x':
    print("Terminating the program...")

# Test Table

# Inputs    Expected     Actual    Comment
#   A,a         -          -         asks user for age of cat in months: ok
#   8 mo    junior/11yo  junior/11yo       ok
#   12 mo   junior/15yo  junior/15yo       ok
#   18 mo   junior/21yo  junior/21yo       ok
#   24 mo   junior/27yo  junior/27yo       ok

#   B,b         -          -         asks user for age of cat in years: ok
#   3yo     prime/28yo   prime/28yo        ok
#   4yo     prime/32yo   prime/32yo        ok
#   5yo     prime/36yo   prime/36yo        ok
#   6yo     prime/40yo   prime/40yo        ok
