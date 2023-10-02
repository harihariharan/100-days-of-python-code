#excercise 1: Functions with outputs

# def format_name(f_name,l_name):
#     f_name = f_name.title()
#     l_name = l_name.title()
#     return f_name+" "+l_name
# f_nam = input("Enter the first name: ")
# l_nam = input("Enter the last name:  ")
# final_name = format_name(f_nam,l_nam)   
# print(final_name)  

#excercise 2: Days in months

# def is_leap(year):
#     if year%400 == 0:
#         return True
#     else:
#         if year%4 == 0:
#             if year%100 != 0:
#                 return True
#             else:
#                 return False  
#         else:
#             return False

# def days_in_months(year,month):
#     if month == 2:
#         leap = is_leap(year)
#         if leap is True:
#             return 29
#         else:
#             return 28
#     else:    
#         month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
#         return month_days[month+1]

# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_months(year,month)
# print(days)

#excercise 3: Combining  dictionaries and function

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
    }
# num1 = int(input("What's the first number?: "))
# num2 = int(input("What's the second number?: "))
# for keys in operations:
#     print(keys)
# operation_symbol = input("Pick an operation from the line above: ")
# calculation_function = operations[operation_symbol]
# answer_1 = calculation_function(num1,num2)

# print(f"{num1} {operation_symbol} {num2} = {answer_1}")

# dec = True
# while dec is True:
#     decision = input("Type 'y' to continue with {answer_1}, or type 'n' to exit.: ").lower()
#     if decision == 'y':
#         operation_symbol = input("Pick another operation: ")
#         num3 = int(input("What's the next number?: "))
#         calculation_function = operations[operation_symbol]
#         answer_2 = calculation_function(answer_1, num3)
#         print(f"{answer_1} {operation_symbol} {num3} = {answer_2}")
#         answer_1 = answer_2
#     else:
#         dec = False
#         print("Thank you.")    
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))  
    for keys in operations:
        print(keys)
    should_continue = True
    while should_continue:    
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("What's the another number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        dec = input(f"Type 'y' to continue with {answer}, or type 'n' to exit, or type 's' to start a new calculation.: ").lower()
        if  dec == 'y':   
            num1 = answer
        elif dec == 's':
            should_continue = False    
            calculator()
        else:
            should_continue = False 
            print("Thank You.")
calculator()            
