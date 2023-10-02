#excercise 1: debugging

############DEBUGGING#####################

# Describe Problem
# def my_function():
#   for i in range(1, 21): //fixed
#     if i == 20:
#       print("You got it")
# my_function()

# Reproduce the Bug
# from random import randint   //fixed
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# Play Computer
# year = int(input("What's your year of birth?"))  //fixed
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# Fix the Errors
# age = int(input("How old are you?"))   //fixed
# if age > 18:
#     print(f"You can drive at age {age}.")

#Print is Your Friend
# pages = 0            //fixed
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
# def mutate(a_list):    //fixed
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

#excercise 2: Debugging odd or even

# number = int(input("which number do you want to check: "))
# if number%2 == 0:
#    print("This is an even number.")
# else:
#    print("This is an odd number.")   

#excercise 3: Debigginng leap year

# year = int(input("Enter the year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not leap year")
#     else:
#         print("Leap year") 
# else:
#     print("Not a Leap year")      

#excercise 4: Debugging FizzBuzz

# for number in range(1,101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)                         