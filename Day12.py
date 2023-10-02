 #excercise 1: The number guessing game

logo = """
   / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
  / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
 / /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
 \____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
 """

import random
print(logo)
print("Welcome to the Number guessing game!!!")
number = random.randint(1,100)   
win = 0 
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ").lower()
if difficulty == 'hard':
     guesses = 5
else:
     guesses = 10

while guesses!=0 and win == 0:    
    print(f"You have {guesses} attempts remaining to guess the number.")
    user_num = int(input("Make a guess: "))
    if user_num > number:
         print("Too High.")
         print("Guess again")
         guesses -= 1
    elif user_num < number:
         print("Too low.")
         print("Guess again")
         guesses -= 1
    elif user_num == number:
         print(f"You got it! The answer was {number}.")
         win = 1
if win == 1:
     print("You win.")
if guesses == 0:
     print("You Lost.")  
     print("You ran out of guesses.")          

