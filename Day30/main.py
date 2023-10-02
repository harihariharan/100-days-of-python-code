#excercise 1: Index error handling

# fruits = ["Apple", "Pear", "Orange"]

# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:    
#         print(fruit + " pie")

# make_pie(4)       

#excercise 2: Key error handling

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]

# total_likes = 0
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         pass    
# print(total_likes)   

#excercise 3: Exception handling in the NATO phonetic alphabets challenge

# import pandas as pd
# data = pd.read_csv("Day26/NATO-alphabet-start/NATO-alphabet-start/nato_phonetic_alphabet.csv")

# result = {row.letter:row.code for (index,row) in data.iterrows()}
# letter = True
# while letter is True:
#     user_input = input("Enter a word: ").upper()
#     try:
#         user_result = [result[letter] for letter in user_input]
#     except KeyError:
#         print("Sorry, only letters in the alphabets please.")    
#     else:    
#         print(user_result) 
#         letter = False