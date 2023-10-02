#excercise 1: Picking a Random words and checking answers

# import random
# word_list = ["ardvark", "baboon", "camel"]
# word = random.choice(word_list)
# letter = input("Guess a letter: ").lower()
# for i in word:
#     if letter == i:
#         print("Right")
#     else:
#         print("Wrong")    

#excercise 2: Replacing blanks with guesses

# import random
# word_list = ["ardvark", "baboon", "camel"]
# display=[]  
# word = random.choice(word_list)
# for _ in range(len(word)):
#     display += "_"
# print(display)  
# letter = input("Guess a letter: ").lower()
# for i in range(len(word)):
#     al = word[i]
#     if al == letter:
#         display[i]= letter  
# print(display)

#excercise 3: Checking if the player has won

# import random
# word_list = ["ardvark", "baboon", "camel"]
# display=[]  
# word = random.choice(word_list)
# for _ in range(len(word)):
#     display += "_"
# print(display)  
# find=0
# while find!=len(word):
#     letter = input("Guess a letter: ").lower()
#     for i in range(len(word)):
#         al = word[i]
#         if al == letter:
#             display[i]= letter  
#             find += 1
#     print(display)
# print("You Win.")    

#excercise 4: Keeping track of the player

# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']

# import random
# word_list = ["ardvark", "baboon", "camel"]
# display=[]  
# lives = 6
# status = "Lose"
# word = random.choice(word_list)
# for _ in range(len(word)):
#     display += "_"  
# while lives != 0:
#     for i in display:
#         print(i+" ",end='')
#     letter = input("\nGuess a letter: ").lower()
#     for i in range(len(word)):
#         al = word[i]
#         if al == letter:
#             display[i] = letter 
#         if letter not in word:  
#             lives -= 1
#             print(stages[lives])
#             break
#     if "_" not in display:
#         status="WIN"
#         print("You Win")
#     if lives == 0:
#         print("You Lose.")  
#     if status == "WIN":
#         lives=0              

#excercise 5: Improving user experience Final HANGMAN

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random
print(logo)
word_list = word_list = [
'abruptly', 
'absurd', 
'abyss', 
'affix', 
'askew', 
'avenue', 
'awkward', 
'axiom', 
'azure', 
'bagpipes', 
'bandwagon', 
'banjo', 
'bayou', 
'beekeeper', 
'bikini', 
'blitz', 
'blizzard', 
'boggle', 
'bookworm', 
'boxcar', 
'boxful', 
'buckaroo', 
'buffalo', 
'buffoon', 
'buxom', 
'buzzard', 
'buzzing', 
'buzzwords', 
'caliph', 
'cobweb', 
'cockiness', 
'croquet', 
'crypt', 
'curacao', 
'cycle', 
'daiquiri', 
'dirndl', 
'disavow', 
'dizzying', 
'duplex', 
'dwarves', 
'embezzle', 
'equip', 
'espionage', 
'euouae', 
'exodus', 
'faking', 
'fishhook', 
'fixable', 
'fjord', 
'flapjack', 
'flopping', 
'fluffiness', 
'flyby', 
'foxglove', 
'frazzled', 
'frizzled', 
'fuchsia', 
'funny', 
'gabby', 
'galaxy', 
'galvanize', 
'gazebo', 
'giaour', 
'gizmo', 
'glowworm', 
'glyph', 
'gnarly', 
'gnostic', 
'gossip', 
'grogginess', 
'haiku', 
'haphazard', 
'hyphen', 
'iatrogenic', 
'icebox', 
'injury', 
'ivory', 
'ivy', 
'jackpot', 
'jaundice', 
'jawbreaker', 
'jaywalk', 
'jazziest', 
'jazzy', 
'jelly', 
'jigsaw', 
'jinx', 
'jiujitsu', 
'jockey', 
'jogging', 
'joking', 
'jovial', 
'joyful', 
'juicy', 
'jukebox', 
'jumbo', 
'kayak', 
'kazoo', 
'keyhole', 
'khaki', 
'kilobyte', 
'kiosk', 
'kitsch', 
'kiwifruit', 
'klutz', 
'knapsack', 
'larynx', 
'lengths', 
'lucky', 
'luxury', 
'lymph', 
'marquis', 
'matrix', 
'megahertz', 
'microwave', 
'mnemonic', 
'mystify', 
'naphtha', 
'nightclub', 
'nowadays', 
'numbskull', 
'nymph', 
'onyx', 
'ovary', 
'oxidize', 
'oxygen', 
'pajama', 
'peekaboo', 
'phlegm', 
'pixel', 
'pizazz', 
'pneumonia', 
'polka', 
'pshaw', 
'psyche', 
'puppy', 
'puzzling', 
'quartz', 
'queue', 
'quips', 
'quixotic', 
'quiz', 
'quizzes', 
'quorum', 
'razzmatazz', 
'rhubarb', 
'rhythm', 
'rickshaw', 
'schnapps', 
'scratch', 
'shiv', 
'snazzy', 
'sphinx', 
'spritz', 
'squawk', 
'staff', 
'strength', 
'strengths', 
'stretch', 
'stronghold', 
'stymied', 
'subway', 
'swivel', 
'syndrome', 
'thriftless', 
'thumbscrew', 
'topaz', 
'transcript', 
'transgress', 
'transplant', 
'triphthong', 
'twelfth', 
'twelfths', 
'unknown', 
'unworthy', 
'unzip', 
'uptown', 
'vaporize', 
'vixen', 
'vodka', 
'voodoo', 
'vortex', 
'voyeurism', 
'walkway', 
'waltz', 
'wave', 
'wavy', 
'waxy', 
'wellspring', 
'wheezy', 
'whiskey', 
'whizzing', 
'whomever', 
'wimpy', 
'witchcraft', 
'wizard', 
'woozy', 
'wristwatch', 
'wyvern', 
'xylophone', 
'yachtsman', 
'yippee', 
'yoked', 
'youthful', 
'yummy', 
'zephyr', 
'zigzag', 
'zigzagging', 
'zilch', 
'zipper', 
'zodiac', 
'zombie', 
]
display=[]  
lives = 6
status = "Lose"
word = random.choice(word_list)
print(word)
for _ in range(len(word)):
    display += "_"  
while lives != 0:
    for i in display:
        print(i+" ",end='')
    letter = input("\nGuess a letter: ").lower()
    if letter in display:
            print("You've already guessed ",letter)
    for i in range(len(word)):
        al = word[i]
        if al == letter:
            display[i] = letter 
        if letter not in word:  
            lives -= 1
            print("You guessed "+letter+", that's not in the word. You lose a life.")
            print(stages[lives])
            break
    if "_" not in display:
        for _ in range(len(word)):
            display += "_"  
        status="WIN"
        print("You Win")
    if lives == 0:
        print("You Lose.")  
    if status == "WIN":
        lives=0    
