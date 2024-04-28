import re

def password_strength_checker (password):
    length= len(password) 
    score=0
    if length >= 8:
      if re.search(r"[A-Z]",password):
         score+=1
      if re.search(r"[a-z]",password):
         score+=1
      if re.search(r"[0-9]",password):
         score+=1
      if re.search(r"[!@#$%^&*()-_+=~`[{}|:;'<>,.?/]",password):
         score +=1
 
      if score>=3:
        print( "Password is accepted")
      else:
        print("Password is denied")
    
    
    else:
       print("password is too short")

user_password=input("Enter your password:")
password_strength_checker(user_password)
