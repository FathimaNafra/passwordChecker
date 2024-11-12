import re
def check_password_strength(password):
    #set initial score
    score=0
    #check length
    if len(password)>=8:
        score +=1
    #check for uppercase letters
    if re.search(r"[A-Z]",password):
        score += 1
    #check for lowercase letters
    if re.search(r"[a-z]",password):
        score += 1
    #chech for digits
    if re.search(r"[0-9]",password):
        score +=1
    #check for special characters
    if re.search(r"[@$!%*?&]",password):
        score +=1
    #determine strength based on score
    if score==5:
        strength="strong"
    elif score>=3:
        strength="moderate"
    else:
        strength ="weak"
    return strength
password=input("enter a password to check its strength:")
strength = check_password_strength(password)
print("password strength:",strength)
