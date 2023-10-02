#excercise 1: Functions with inputs

# def greet():
#     print("Hello");
#     print("Hari");
#     print("Haran J")
# greet()    

#excercise 2:  Paint Area calculator

# import math
# def print_calc(height,width,cover):
#     number_of_cans = math.ceil((height*width)/cover)
#     print(f"You'll need {number_of_cans} cane of paint")
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall:  "))
# coverage = 5
# print_calc(height=test_h, width=test_w, cover=coverage)

#excercise 3: Prime number checker

# def prime_checker(number):
#     if number == 2 or number == 1:
#         text = "It's a prime number"
#         return text
#     for i in range(2,number):
#         if number%i == 0:
#             text = "It's not a prime number"
#             return text
#     text = "It's a prime number"
#     return text    

# n = int(input("Checck this number: "))
# text = prime_checker(number = n)
# print(text)

#excercise 4: Ceaser ciper (all the four challenges)

# def Encrypt(text,shift):
#     encrypt_word = ""
#     s_char = True
#     passage = []
#     for letter in text:
#         s_char = True
#         for i in range(0,len(alphabet)):
#            if alphabet[i] == letter:
#                encrypt_word += alphabet[i+shift]     
#                s_char=False
#         if s_char is True:
#            encrypt_word += letter 
#     return encrypt_word   

# def Decrypt(text,shift):
#     decrypt_word = ""
#     s_char = True
#     passage = []
#     for letter in text:
#         s_char = True
#         for i in range(0,len(alphabet)):
#            if alphabet[i] == letter:
#                decrypt_word += alphabet[i-shift]     
#                s_char=False
#         if s_char is True:
#            decrypt_word += letter 
#     return decrypt_word  

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           

"""   

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def Cipher(text,shift,code):
    crypt_word = ""
    if code == "decode":
         shift *= -1   
    for letter in text:
        if letter not in alphabet:
            crypt_word += letter
        else:    
            pos = alphabet.index(letter)
            new_pos = pos + shift
            crypt_word += alphabet[new_pos]
    print(f"Here's the {code}d result: {crypt_word}")

print(logo)
status = True
while status is True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) 
    shift = shift%26
    Cipher(text,shift,code = direction)  
    state = input("Do you want to continue? Type 'yes' for Yes and 'no' for No? ").lower()
    if state == "no":
        status = False
        print("Thank you.")