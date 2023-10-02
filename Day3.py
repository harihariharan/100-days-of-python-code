#exercise 1:

# number = int(input("Which number do you want to check? "))
# if number%2 == 0:
#     print("This nuumber is an even number")
# else:
#     print("This nuumber is an odd number")   

#exercise 2: BMI 2.0

# height = float(input("Enter your height in m:"))
# weight = float(input("Enter your weight in kg:"))
# BMI = weight/(height*height)
# BMI = round(BMI,2)
# if BMI<=18.5:
#     comment = "under weight"
# elif BMI<25:
#     comment = "normal weight"
# elif BMI<30:
#     comment = "over weight"
# elif BMI<35:
#     comment = "obese"
# else:
#     comment = "clinically obese"        
# print(f"your BMI is {BMI}, you are {comment}")

#exercise 3: Leap year

# year = int(input("Which year do you want to check? "))
# if year%400 == 0:
#     print("Leap year")
# else:
#     if year%4 == 0:
#         if year%100 != 0:
#             print("Leap year")
#         else:
#             print("Not a Leap year")   
#     else:
#         print("Not a leap year")  

#exercise 4: pizza order 

# print("Welcome to python pizza deliveries!")
# size = input("What size pizza do you want? S, M, L : ")
# add_pepperoni = input("Do you want add_pepperoni? Y or N : ")
# extra_cheese = input("Do you want extra cheese? Y or N :")
# final_bill = 0
# if size == "S":
#     final_bill += 15
#     if add_pepperoni == "Y":
#         final_bill += 2  
# elif size == "M":
#     final_bill += 20
#     if add_pepperoni == "Y":
#         final_bill += 3   
# else:
#     final_bill +=25
#     if add_pepperoni == "Y":
#         final_bill += 3
# if extra_cheese == "Y":
#         final_bill += 1
# print(f"Your final bill is: Rs.{final_bill}")          

#excercise 5: Love calculator

# print("Welcome to the Love calculator:")
# name1 = input("What is your name: ")
# name2 = input("What is their name:")  
# name = name1 + name2
# name2 = name.lower()
# count_t = count_l = 0
# count_t += name.count("t")
# count_t += name.count("r")
# count_t += name.count("u")
# count_t += name.count("e")

# count_l += name.count("l")
# count_l += name.count("o")
# count_l += name.count("v")
# count_l += name.count("e")

# score = count_t*10 + count_l
# if score<10 or score>96:
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif score>40 and score<50:
#     print(f"Your score is {score}, you are alright together.")
# else:        
#     print(f"Your score is {score}")
          
#excercise 6:Treasure island

print("Welcome to Treasure island.")
print("Your mission is to find the treasure.")
direction = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\" :")
if direction == "left":
    decision = input("You come to lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across : ")
    if decision == "wait":
        door = input("you arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? : ")
        if door =="yellow":
            print("You find the treasure. You Win!!!")
        elif door == "red":
            print("Burned by fire. Game over.")
        elif door == "blue":
            print("Eaten by beasts. game over.")    
        else:
            print("Game Over.") 
    else:
       print("Attacked by trout. Game Over.")      
else:
    print("You fell into a hole. Game Over.")    