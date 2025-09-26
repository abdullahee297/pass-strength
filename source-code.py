import string 
import getpass

def check_pass():
    password = getpass.getpass("Enter password: ")
    
    strength = 0
    
    low_case = up_case = sp_char = digit = puntuat = space = 0
    
    for char in list(password):
        if char in string.ascii_lowercase:
            low_case += 1
        elif char in string.ascii_uppercase:
            up_case += 1
        elif char in string.digits:
            digit += 1
        elif char in string.punctuation:
            puntuat += 1
        elif char.isspace():
            space += 1
        else:
            sp_char += 1
            
    for flag in [low_case, up_case, sp_char, digit, space, puntuat]:
        if flag:
            strength += 1
    
    if len(password) >= 8:
        strength +=2
    elif len(password) >= 4:
        strength += 1
    
    if strength <= 3:
        print("Weak Pasword")
    elif   4 <= strength <= 6:
        print("Meduim Pasword")
    else:
        print("Strong password")
        

if __name__ == "__main__":
    check_pass()