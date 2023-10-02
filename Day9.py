#excercise 1: Grading program

# students_scores = {"Harry" : 81,
#                    "Ron"   : 78,
#                    "Hermione" : 99,
#                    "Draco" : 74,
#                    "Neville" : 62,} 
# student_grades = {}
# for keys in students_scores:
#     if students_scores[keys]>=91:
#         student_grades[keys] = "Outstanding" 
#     elif students_scores[keys]>=81:
#         student_grades[keys] = "Exceeds Expectations" 
#     elif students_scores[keys]>=71:
#         student_grades[keys] = "Acceptable" 
#     else:
#         student_grades[keys] = "Fail"             
# print(student_grades)

#excercise 2: Dictionary in list

# travel_log = [
#     {
#         "country": "France",
#         "visits" : 12,
#         "cities" : ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits" : 5,
#         "cities" : ["Berlin", "Hamburg", "Stuttgart"]
#     }
# ]
# def add_new_country(coun,visit,city):
#     # new_log={}
#     # new_log["country"] = coun
#     # new_log["visits"]  = visit
#     # new_log["cities"]  = city
#     new_log={"country":coun,"visits":visit,"cities":city}
#     travel_log.append(new_log)
    
# add_new_country("Russia",2,["Moscow", "Saint Petersburg"])
# print(travel_log)

#excercise 3: The secret auction program 

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|.-._,.---------.,_.-.
                          |       | | |               | | ''-.
                          |       || |             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the secret auction program.")
dec = True
total_bid = {}
while dec is True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: "))
    total_bid[name] = bid
    decision = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if decision == "no":
        dec = False
highest_bid = 0      
winner = ""  
for name in total_bid:
    bid_amount = total_bid[name] 
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = name
print(f"The winner is {winner} with a bid of {highest_bid}")        