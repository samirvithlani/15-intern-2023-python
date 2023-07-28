no = int(input("Enter a number: "))
sum=0
# for i in range(1,no+1):
    
#     if i %2 ==0:
#         print("even",i)
#     else:
#         print("odd",i) 


for i in range(1,no+1):
    #0 = 0 + 1 = 1
    #1  = 1 + 2 = 3
    #3 = 3 + 3 = 6
    #6 = 6 + 4 = 10
    #10 = 10 + 5 = 15           
    sum = sum + i
    
print("sum of num = ",sum)    