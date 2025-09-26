from zxcvbn import zxcvbn
import getpass

def check_password_strength():
    password = getpass.getpass("Enter password: ")

    result = zxcvbn(password)
    
    score = result['score']
    
    if score == 0:
        scr = 'Very Weak'
    elif score == 1:
        scr = 'Weak'
    elif score == 2:
        scr = 'meduim'
    elif score == 3:
        scr = 'Strong'
    elif score == 4:
        scr = 'Very Strong'


    print("\n🔒 Password Strength Analysis")
    print("-" * 30)
    print(f"Your password is {result['score']} {scr}")
    

if __name__ == "__main__":
    check_password_strength()
