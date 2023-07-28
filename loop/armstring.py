no = int(input("Enter a number: ")) 
temp = no
rem =0
sum =0
while no>0:
    
    rem = no % 10
    sum = sum + rem * rem * rem
    no = no // 10

if temp == sum:
    print("it is a armstrong number")

else:
    print("it is not a armstrong number")       