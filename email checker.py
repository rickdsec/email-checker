import re 

f = open("email list.txt","r+")
emailstr = f.read()

# print(emaillist)



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
email = emailstr

#convert string to list
def Convert(string): 
    li = list(string.split("\n")) 
    return li 

emaillist = Convert(email) 

#loop
for x in emaillist:
   #print(x)
   check(x)

# calling run function  
#check(email) 
  
f.close()   
  
    
