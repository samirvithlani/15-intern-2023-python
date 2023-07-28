no = int(input("Enter a number: "))  # 123 1 + 2 + 3 = 6
#123  123 %10 = 3 no = no // 10 = 12
# 12  12 %10 = 2 no = no // 10 = 1
# 1  1 %10 = 1 no = no // 10 = 0

rem =0
sum =0
mul=1
#12>0
#1>0
#0>0
while no>0:
    rem = no % 10 #123 % 10 3
                  #12 % 10 = 2  
                  #1 % 10 = 1
    sum = sum + rem # 0 + 3 = 3
                    # 3 + 2 = 5  
                    # 5 + 1 = 6
    mul = mul * rem                
    no = no // 10 # 123 // 10 = 12
                    # 12 // 10 = 1
                    # 1 // 10 = 0

print("sum of digit = ",sum)                    
print("mul of digit = ",mul)
    
    
if sum == mul:
    print("it is a twin number")    
else:
    print("it is not a twin number")    
    
