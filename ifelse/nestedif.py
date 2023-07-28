age = int(input("Enter your age: "))
#70
if age>=18:
    print("You are eligible to vote")
    
    if age>=60:
        print("You are eligible for senior citizen")
    else:
        print("You are not eligible for senior citizen")    
        
    if age>=21:
        print("You are eligible to marrige")    
    
    else:
        print("You are not eligible to marrige")    

else:
    print("You are not eligible to vote")
    
    if age>=14:
        print("You are eligible for learning licence")
    
    else:
        print("You are not eligible for learning licence")
                