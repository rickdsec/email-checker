import re 
  

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
      
# Define a function for 
# for validating an Email 
def check(email):  
  
    # pass the regualar expression 
    # and the string in search() method 
    if(re.search(regex,email)):  
        print("Email goedgekeurd!")  
          
    else:  
        print("Email afgekeurd!")  
      
  

      
# Enter the email  
email = input("Typ je email hier  ")
      
    # calling run function  
check(email) 
  
    
  
    
