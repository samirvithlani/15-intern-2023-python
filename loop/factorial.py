no = int(input("Enter a number: ")) # 5  *4 *3*2*1 = 120
fact = 1
for i in range(1,no+1): 
    #1 = 1 * 1 = 1
    #1 = 1 * 2 = 2 
    #2 = 2 * 3 = 6
    #6 = 6 * 4 = 24
    #24 = 24 * 5 = 120
    fact = fact * i

print("factorial of num = ",fact)    