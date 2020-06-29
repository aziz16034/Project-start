import random


#username and email generator
full_name = input("Please enter your name: ")
names = full_name.split(" ")
if (len(names) <= 1):
     print("Please input your full name")
     exit() 
first_letter = names[0][0]
firstletter = first_letter.lower()
three_letters_surname = names[1][0:]
surname = three_letters_surname.lower()
number = '{:03d}'.format(random.randrange (1,999))
username = "".join([surname, firstletter, str(number)])
print("This is your username: ", username)
print("Your email address: ", username,"@beloit.edu")

# Password Generator
def password_check(passwd): 
      
    SpecialSym =['$', '@', '#', '%', '!'] 
    val = True
      
    if len(passwd) < 6: 
        print('length should be at least 6') 
        val = False
          
    if len(passwd) > 20: 
        print('length should be not be greater than 8') 
        val = False
          
    if not any(char.isdigit() for char in passwd): 
        print('Password should have at least one numeral') 
        val = False
          
    if not any(char.isupper() for char in passwd): 
        print('Password should have at least one uppercase letter') 
        val = False
          
    if not any(char.islower() for char in passwd): 
        print('Password should have at least one lowercase letter') 
        val = False
          
    if not any(char in SpecialSym for char in passwd): 
        print('Password should have at least one of the symbols $@#') 
        val = False
    if val: 
        return val 

passwde  = str (input("Please choose a strong with standard feature:"))
paswade2 = input("Please type again:")


if passwde ==paswade2:
      
      if (password_check(passwde)): 
        print("Password is valid") 
      else: 
        print("Invalid Password !!") 


else:
     print("password not equal")

 


 #GUI
