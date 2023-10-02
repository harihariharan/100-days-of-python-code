#excercise 1: Average Height

# student_heights = input("Input a list of student heights: ").split()
# for height in range(0,len(student_heights)):
#     student_heights[height] = int(student_heights[height])
# print(student_heights)    
# total_height = 0
# count = 0
# for heights in student_heights:
#     total_height += heights
#     count += 1
# average_height = total_height/count     
# print("Average height: ",round(average_height))

#excercise 2: Highest score

# student_scores = input("Input a list of student heights: ").split()
# for score in range(0,len(student_scores)):
#     student_scores[score] = int(student_scores[score])
# print(student_scores)
# highest_score = student_scores[0]
# for scores in student_scores:
#     if highest_score<scores:
#         highest_score=scores
# print("The highest score in the class is: ",highest_score)  

#excercise 3: Adding even numbers      

# sum = 0
# for i in range(0,101,2):
#     sum += i
# print("Sum: ",sum)    

#excercise 4: FizzBuzz Job interview

# for i in range(1,101):
#     if i%3 == 0 and i%5 == 0:
#         print("FizzBuzz")
#     elif i%3 == 0:
#         print("Fizz")
#     elif i%5 == 0:
#         print("Buzz")
#     else:
#         print(i)       

#excercise 5: Create a password Generator

# import random
# letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
#            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# numbers = ['0','1','2','3','4','5','6','7','8','9']
# symbols = ['!','@','#','$','%','&','(',')','*','+']
# print("Welcome to the PyPassword Generator!")     
# nr_letters = int(input("How many letters would you like in your password? "))
# nr_symbols = int(input("How many symbols would you like in your password? "))
# nr_numbers = int(input("How many numbers would you like in your password? "))

# #Easy level
# # letter=""
# # for i in range(0,nr_letters):
# #     letter += random.choice(letters)
# # for i in range(0,nr_symbols):
# #     letter += random.choice(symbols)
# # for i in range(0,nr_numbers):
# #     letter += random.choice(numbers)           
# # print("Your Generated Password is :",letter) 

# #Hard level
# password=[]
# for i in range(0,nr_letters):
#     password.append(random.choice(letters))
# for i in range(0,nr_symbols):
#     password.append(random.choice(symbols))
# for i in range(0,nr_numbers):
#     password.append(random.choice(numbers))   
# print("\nYour Generated Password is : ",end="")
# random.shuffle(password)
# for word in password:
#     print(word,end="")  