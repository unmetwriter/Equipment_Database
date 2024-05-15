class verificationProcess():
    def __init__(self):
        pass
    
    # Function to verify the credibility of someones social security number. 
    # Checks for:
    # - if a number is given
    # - if the number contains any extra information
    # - if it is valid according to Swedish law.
    # - If it is the correct lenght
    def verify_person_number(self,number : str, errors : list) -> list:
        if(number == ""):
            errors.append("No number given")
        print(number)
        if("-" in number):
            number = number.replace("-","",1)
            print(number)
        print(number)
        if(len(number) == 12):
            number = number[2:]
        
        if(number.isdigit() == False):
            errors.append("Social security number contains non-digits")
        print(number)    
        if(len(number) != 10):
            errors.append("Incorrect length on social security number")
        if(errors == []):
            errors.append(verification_algorithm(number))
        return errors
    
    # Function to verify someones name 
    # Checks for:
    # - Their name is not longer than 250 characters
    # - Their name has numbers in it
    def verify_name(self, name : str, errors : list) -> list:
        if(has_numbers(name)):
            errors.append("Number in name")
        if(len(name) > 250):
            errors.append("Name too long by " + str(len(name)-250))
        if(" " not in name):
            errors.append("Only one name")
        return errors
    
    # Function to verify someones email
    # Checks if:
    # - If they have a @ in their email
    # - Their email is too long
    def verify_email(self, email : str, errors : list) ->list:
        if("@" not in email):
            errors.append("No @ in email adress")
        
        if(len(email) > 250):
            errors.append("email too long by " + str(len(email)-250))
        
        return errors
        
    def verify_phone_number(self, number : str, errors : list) -> list:
        if(number.isdigit() == False):
            errors.append("Phone number contains non-digits")
            
        if(len(number) != 10):
            errors.append("Phone number incorrect lenght")
        if(number.isdigit()):
            if(int(number[0])!= 0):
                errors.append("Phone number starts with the wrong number")

        return errors
    
# Help function that checks if a string has numbers in it
def has_numbers(inputString : str) -> bool:
    return any(char.isdigit() for char in inputString)
    
# Algorithm that checks if a social security number is correct
def verification_algorithm(number : str) -> list:
    sum : int = 0
    for i in range(9):
        if (i % 2 == 0 or i == 0):    
            temp = (int(number[i])*2)
            if(temp > 9):
                sum = sum + 1 +(temp%10)
            else:
                sum = sum + temp
        if (i % 2 == 1):
            sum = sum + int(number[i])    
    if ((sum + int(number[9]))%10 == 0):   
        return 
    return "Social Security number is invalid"