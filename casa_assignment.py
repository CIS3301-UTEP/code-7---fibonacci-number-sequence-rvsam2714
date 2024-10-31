import re
user_pass = input("Please enter your password:")
def test_password(password):
    level_0 = re.findall(r"^\S{8,}$",password)
    level_1 = re.findall(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*#?&]{8,}$", password)
    level_2 = re.findall(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$",password)
    level_3 = re.findall(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",password)
    if len(level_0) > 0:
        if len(level_1) > 0:
            if len(level_2) > 0:
                if len(level_3) > 0 :
                    print("Your password is level 3")
                else:
                    print("Your password is level 2")
            else:
                print("Your password is level 1")
        else:
            print("Your password is level 0")


            
            
                
                    
        


test_password(user_pass)
