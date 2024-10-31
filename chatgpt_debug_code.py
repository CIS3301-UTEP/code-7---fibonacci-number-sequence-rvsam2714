# import re
# def test_password(password):
#     print(f"Input password: '{password}'")
    
#     level_0 = re.findall(r"^\S{8,}$", password)
#     print(f"Level 0 matches: {level_0}")  # Debug print
    
#     level_1 = re.findall(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", password)
#     print(f"Level 1 matches: {level_1}")  # Debug print
    
#     level_2 = re.findall(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$", password)
#     print(f"Level 2 matches: {level_2}")  # Debug print
    
#     level_3 = re.findall(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password)
#     print(f"Level 3 matches: {level_3}")  # Debug print
    
#     if len(level_0) > 0:
#         if len(level_1) > 0:
#             if len(level_2) > 0:
#                 if len(level_3) > 0:
#                     print("Your password is level 3")
#                 else:
#                     print("Your password is level 2")
#             else:
#                 print("Your password is level 1")
#         else:
#             print("Your password is level 0")
#     else:
#         print("Your password is level 0")
# test_password('111aaa!!!AAA')
import re

user_pass = input("Please enter your password: ")

def test_password(password):
    print(f"Input password: '{password}'")
    
    level_0 = re.findall(r"^\S{8,}$", password)
    print(f"Level 0 matches: {level_0}")  # Debug print
    
    level_1 = re.findall(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*#?&]{8,}$", password)
    print(f"Level 1 matches: {level_1}")  # Debug print
    
    level_2 = re.findall(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$", password)
    print(f"Level 2 matches: {level_2}")  # Debug print
    
    level_3 = re.findall(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password)
    print(f"Level 3 matches: {level_3}")  # Debug print
    
    if len(level_0) > 0:
        if len(level_1) > 0:
            if len(level_2) > 0:
                if len(level_3) > 0:
                    print("Your password is level 3")
                else:
                    print("Your password is level 2")
            else:
                print("Your password is level 1")
        else:
            print("Your password is level 0")
    else:
        print("Your password is level 0")

test_password(user_pass)

