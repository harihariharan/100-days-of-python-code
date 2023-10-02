#excercise 1: Flipping of coin

# import random
# flip = random.randint(0,1)
# if(flip == 0):
#     print("Tail")
# else:
#     print("Head")    

#excercise 2: Banker Roulette - who will pay the bill?

# import random
# names_string = input("Give me everybody's names, separated by a comma : ")
# names = names_string.split(", ")
# # length = len(names)
# # people = random.randint(0,length-1)
# # man = names[people]
# man = random.choice(names)
# print(f"{man} is going to buy the meal today!")

#excercise 3: Treasure Map

# row1 = [0,0,0]
# row2 = [0,0,0]
# row3 = [0,0,0]
# map = [row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# coloumn = int(position[0])-1
# row = int(position[1])-1
# map[row][coloumn] = "X"
# print(f"{row1}\n{row2}\n{row3}")

#excercise 3: Rock Paper Scissors 

# import random
# man_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors : "))
# choices = ["Rock", "Paper", "Scissors"]
# m_choice = choices[man_choice]
# print(f"Man choice: {m_choice}")
# # if man_choice == 0:
# #     print("man_choice: Rock")
# # elif man_choice == 1:
# #     print("man_choice: Paper")
# # else:
# #     print("man_choice: Scissors")        
# computer_choice = random.randint(0,2)
# com_choice = choices[computer_choice]
# print(f"Computer choice: {com_choice}")
# # if computer_choice == 0:
# #     print("computer_choice: Rock")
# # elif computer_choice == 1:
# #     print("computer_choice: Paper")
# # else:
# #     print("computer_choice: Scissors")  
# if man_choice == computer_choice:
#     print("Result: Match Tied")
# elif (man_choice == 0 and computer_choice == 1) or (man_choice == 2 and computer_choice == 0) or (man_choice == 1 and computer_choice == 2):
#     print("Result: Computer Wins!!!")
# elif (man_choice == 0 and computer_choice == 2) or (man_choice == 1 and computer_choice == 0) or (man_choice == 2 and computer_choice == 1):
#     print("Result: You Win!!!")        

